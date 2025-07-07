import os
import time
import math
import pandas as pd
from PIL import Image
import torch
import numpy as np
from pathlib import Path
import platform
from dotenv import load_dotenv
from transformers import AutoProcessor, AutoModelForZeroShotObjectDetection
from segment_anything import sam_model_registry, SamPredictor
import torchvision.ops as ops  # For NMS
from annotation_utils import get_image_info, create_coco_from_absolute_boxes, annotation_to_json, print_stats, sleep_visually

# ---------------------------
# Setup Paths & Environment
# ---------------------------
if platform.system() == "Darwin":  # macOS
    BASE_PATH = "..."
    env_path = Path(".../.env")
elif platform.system() == "Linux":
    BASE_PATH = "..."
    env_path = Path(".../.env")
else:
    raise OSError("Unsupported operating system detected.")

load_dotenv(dotenv_path=env_path)

# Define the metadata CSV path and base image directory.
METADATA_FILE = os.path.join(BASE_PATH, "metadata/dataset.csv")
BASE_DIR = BASE_PATH
print(f"✅ Using BASE_PATH: {BASE_PATH}")

# ---------------------------
# Configuration
# ---------------------------
_time_to_sleep_between_intervals = 10  # ORI 10

IMAGE_TO_PROCESS = 250  # Number of images to preannotate per batch
USE_SAM = False        # Switch: False to use DINO-only improvement.
# Thresholds for DINO and SAM
DINO_BOX_THRESHOLD = 0.25  # Lowering it will make DINO propose more boxes
CONFIDENCE_THRESHOLD_TO_USE_FOR_SAM = 0.2  # Only boxes above this score will be used
_box_expansion = 0.025  # Increase size of boxes refined by SAM in %
_text_threshold = 0.3
box_area_image_area = 0.4
_iou_threshold = 0.9
_containment_tolerance = 0.05

PROMPTS = [
    "a real, living bird with natural feathers and a clearly visible beak (not an illustration)",
    "a small, wild bird naturally perched among branches and partially hidden by leaves",
    "a genuine bird, such as a woodpecker, clinging to a tree trunk with authentic, natural plumage",
    "a bird in flight with clearly visible wings and dynamic posture",
    "a bird with a distinctive head shape and prominent eyes, captured in high detail",
    "a bird at close range showing detailed feather patterns and natural colors",
    "a small, grayish bird with a black or dark cap, perched among branches or on a roof, partially hidden, with natural feathers and a short beak",

]


# ---------------------------
# Load CSV + print Stats
# ---------------------------
df = pd.read_csv(METADATA_FILE, keep_default_na=False)
print_stats(df, label="STATE BEFORE PREANNOTATION")

# ---------------------------
# DINO+SAM Setup
# ---------------------------
MODEL_ID = "IDEA-Research/grounding-dino-base"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
SAM_CHECKPOINT_PATH = os.path.join(BASE_PATH, "models/sam_vit_h_4b8939.pth")

processor = AutoProcessor.from_pretrained(MODEL_ID)
dino_model = AutoModelForZeroShotObjectDetection.from_pretrained(MODEL_ID).to(DEVICE)

# SAM is still loaded but will only be used if USE_SAM is True.
sam = sam_model_registry["vit_h"](checkpoint=SAM_CHECKPOINT_PATH).to(DEVICE)
predictor = SamPredictor(sam)


# ---------------------------
# Define DINO Functions (with Ensemble Prompts)
# ---------------------------

def filter_nested_boxes(boxes, iou_threshold=0.9, containment_tolerance=0.05):
    """
    Filters out boxes that are nearly completely overlapping (IoU above threshold)
    or that are completely contained within a larger box (with a small tolerance).
    """
    filtered = []
    for i, box in enumerate(boxes):
        x1, y1, x2, y2, score = box
        keep = True
        for j, other in enumerate(boxes):
            if i == j:
                continue
            ox1, oy1, ox2, oy2, other_score = other

            # Check full containment with tolerance.
            if (x1 >= ox1 - containment_tolerance and
                    y1 >= oy1 - containment_tolerance and
                    x2 <= ox2 + containment_tolerance and
                    y2 <= oy2 + containment_tolerance and
                    other_score >= score):
                keep = False
                break

            # Compute IoU.
            inter_x1 = max(x1, ox1)
            inter_y1 = max(y1, oy1)
            inter_x2 = min(x2, ox2)
            inter_y2 = min(y2, oy2)
            inter_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)
            area1 = (x2 - x1) * (y2 - y1)
            area2 = (ox2 - ox1) * (oy2 - oy1)
            union_area = area1 + area2 - inter_area
            iou = inter_area / union_area if union_area > 0 else 0

            if iou > iou_threshold and other_score >= score:
                keep = False
                break
        if keep:
            filtered.append(box)
    return filtered


def process_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image_width, image_height = image.size
    image_area = image_width * image_height

    if not USE_SAM:
        combined_boxes = []
        # Run detection with each prompt.
        for prompt in PROMPTS:
            inputs = processor(images=image, text=prompt, return_tensors="pt").to(DEVICE)
            with torch.no_grad():
                outputs = dino_model(**inputs)
            results = processor.post_process_grounded_object_detection(
                outputs=outputs,
                input_ids=inputs.input_ids,
                box_threshold=DINO_BOX_THRESHOLD,
                text_threshold=_text_threshold,
                target_sizes=[image.size[::-1]],  # (height, width)
            )
            for result in results:
                boxes = result["boxes"]
                scores = result["scores"]
                for box, score in zip(boxes, scores):
                    if score < CONFIDENCE_THRESHOLD_TO_USE_FOR_SAM:
                        continue
                    x_min, y_min, x_max, y_max = map(int, box.tolist())
                    # Calculate box area and compare to image area.
                    box_area = (x_max - x_min) * (y_max - y_min)
                    if box_area / image_area >= box_area_image_area:
                        # Skip boxes that fill more than 95% of the image.
                        continue
                    combined_boxes.append((x_min, y_min, x_max, y_max, float(score)))
        # Fuse boxes using non-maximum suppression (NMS).
        if combined_boxes:
            boxes_tensor = torch.tensor([[b[0], b[1], b[2], b[3]] for b in combined_boxes], dtype=torch.float32)
            scores_tensor = torch.tensor([b[4] for b in combined_boxes], dtype=torch.float32)
            keep_indices = ops.nms(boxes_tensor, scores_tensor, iou_threshold=0.5)
            fused_boxes = [combined_boxes[i] for i in keep_indices]
            # Filter out nested boxes.
            fused_boxes = filter_nested_boxes(fused_boxes, iou_threshold=_iou_threshold, containment_tolerance=_containment_tolerance)
        else:
            fused_boxes = []
        return image, fused_boxes
    else:
        # SAM branch.
        inputs = processor(images=image, text="a bird", return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            outputs = dino_model(**inputs)
        results = processor.post_process_grounded_object_detection(
            outputs=outputs,
            input_ids=inputs.input_ids,
            box_threshold=DINO_BOX_THRESHOLD,
            text_threshold=_text_threshold,
            target_sizes=[image.size[::-1]],
        )
        combined_boxes = []
        for result in results:
            # Check if result is a dict or tuple/list
            if isinstance(result, dict):
                boxes = result["boxes"]
                scores = result["scores"]
            elif isinstance(result, (tuple, list)):
                # Assuming boxes are at index 0 and scores at index 1.
                boxes, scores = result[0], result[1]
            else:
                raise ValueError("Unexpected format of detection result")

            for box, score in zip(boxes, scores):
                if score < CONFIDENCE_THRESHOLD_TO_USE_FOR_SAM:
                    continue
                x_min, y_min, x_max, y_max = map(int, box.tolist())
                box_area = (x_max - x_min) * (y_max - y_min)
                if box_area / image_area > box_area_image_area:
                    continue
                combined_boxes.append((x_min, y_min, x_max, y_max, float(score)))

        return image, results

def refine_with_sam(image, results, box_expansion=0.01):
    """
    Refines DINO detections using SAM.
    Returns a list of refined bounding boxes in the format:
      (x_min, y_min, x_max, y_max, score)
    """
    predictor.set_image(np.array(image))

    def expand_box(x_min, y_min, x_max, y_max, expansion=0.01):
        w = x_max - x_min
        h = y_max - y_min
        cx = x_min + w / 2
        cy = y_min + h / 2
        new_w = w * (1 + expansion)
        new_h = h * (1 + expansion)
        new_x_min = math.floor(cx - new_w / 2)
        new_y_min = math.floor(cy - new_h / 2)
        new_x_max = math.ceil(cx + new_w / 2)
        new_y_max = math.ceil(cy + new_h / 2)
        return new_x_min, new_y_min, new_x_max, new_y_max

    refined_boxes = []
    for result in results:
        boxes = result["boxes"]
        scores = result["scores"]
        for box, score in zip(boxes, scores):
            if score < CONFIDENCE_THRESHOLD_TO_USE_FOR_SAM:
                continue
            x_min, y_min, x_max, y_max = map(int, box.tolist())
            sam_box = np.array([x_min, y_min, x_max, y_max])
            masks, sam_scores, _ = predictor.predict(box=sam_box)
            best_mask_idx = sam_scores.argmax()
            best_mask = masks[best_mask_idx]
            ys, xs = np.where(best_mask)
            if len(xs) == 0 or len(ys) == 0:
                print(f"Warning: No pixels detected for box: {(x_min, y_min, x_max, y_max)}. Skipping annotation.")
                continue
            x_min_refined, y_min_refined = int(xs.min()), int(ys.min())
            x_max_refined, y_max_refined = int(xs.max()), int(ys.max())
            refined_box = (x_min_refined, y_min_refined, x_max_refined, y_max_refined)
            expanded_box = expand_box(*refined_box, expansion=box_expansion)
            print(f"Original box: {(x_min, y_min, x_max, y_max)}, Refined box: {refined_box}, Expanded box: {expanded_box}")
            refined_boxes.append((*expanded_box, float(score)))
    return refined_boxes

# ---------------------------
# Main Loop: Process in Batches
# ---------------------------
print("\n🔄 Starting batch processing (preannotation) ...")

total_time = 0.0
processed_count = 0

while True:
    # Reload the CSV to reflect newly processed images.
    df = pd.read_csv(METADATA_FILE, keep_default_na=False)
    unprocessed = df[df["preannotation"].str.strip() == "no"].copy()
    if not unprocessed.empty:
        pre_batch = unprocessed.head(IMAGE_TO_PROCESS)
        for idx, row in pre_batch.iterrows():
            image_path = os.path.join(BASE_DIR, row["image_path"])
            print(f"\nPreannotating image: {image_path}")
            start_time = time.time()
            try:
                if USE_SAM:
                    image, results = process_image(image_path)
                    boxes = refine_with_sam(image, results, box_expansion=_box_expansion)
                else:
                    image, boxes = process_image(image_path)
            except Exception as e:
                print(f"Error during detection on {image_path}: {e}")
                continue

            try:
                image_info = get_image_info(image_path)
            except Exception as e:
                print(f"Error reading image metadata for {image_path}: {e}")
                continue

            species_label = row["species"].strip()
            categories = {species_label: 1}  # Assume a single category per image

            # Convert bounding boxes (absolute coordinates) into COCO format.
            coco_annotation = create_coco_from_absolute_boxes(image_info, boxes, categories)
            annotation_json = annotation_to_json(coco_annotation)

            # Update the CSV with the new preannotation (format remains consistent regardless of the switch)
            df.at[idx, "preannotation"] = annotation_json

            current_time = time.time() - start_time
            total_time += current_time
            processed_count += 1
            avg_time = total_time / processed_count
            print(f"Total images processed: {processed_count}. Time for current image: {current_time:.2f} sec, Average time: {avg_time:.2f} sec")

        # Save the updated CSV.
        df.to_csv(METADATA_FILE, index=False)
        print("✅ Preannotation batch completed and CSV updated.")
    else:
        print("\nℹ️  No images left to preannotate.")
        break

    print_stats(pd.read_csv(METADATA_FILE, keep_default_na=False), label="STATE AFTER PREANNOTATION")

    try:
        print("\n⏳ Sleeping for 10 seconds. Press Ctrl+C to stop execution if needed...")
        sleep_visually(_time_to_sleep_between_intervals)
    except KeyboardInterrupt:
        print("\n🛑 Execution stopped by user.")
        break

# ---------------------------
# Print Stats After Run
# ---------------------------
df = pd.read_csv(METADATA_FILE, keep_default_na=False)
print_stats(df, label="STATE AFTER RUN")
print("\n✅ Completed: All batches processed and CSV updated.")