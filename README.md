# WatchMyBirds-Data

This dataset (11859 annotated images) is designed to train the models behind [**WatchMyBirds**](https://github.com/arminfabritzek/WatchMyBirds) – a lightweight, customizable object detection system tailored for real-time monitoring. Built with PyTorch and TensorFlow, WatchMyBirds supports live video streaming, automatic frame capture based on detection criteria, and Telegram integration for timely notifications. Images in the dataset may contain different species, and all annotations are provided in COCO format.

Built for **hobbyists, researchers, and wildlife enthusiasts**, WatchMyBirds makes real-time monitoring **accessible and powerful**. 🚀  

---

![](stats/sample_images_with_bboxes.png)

---

![](stats/approved_annotations_per_species.png)

---

![](stats/jointplot_center_xy.png)

---

![](stats/jointplot_width_height.png)

---

## Dataset CSV Preview (First 4 Lines)

| original_url                                                                 | attribution                                    | image_hash                       | approved_annotation                                                                                                                                                                                                                                                                                                                                                         |
|:-----------------------------------------------------------------------------|:-----------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| https://inaturalist-open-data.s3.amazonaws.com/photos/234664642/original.jpg | (c) Sem Khatov, some rights reserved (CC BY)   | e240477e4aff5ad4a19f728a536d4efe | {"annotations": [{"id": 153135281001, "image_id": 153135281, "category_id": 8, "bbox": [958.0, 401.0, 189.0, 355.0], "area": 67095.0, "iscrowd": 0}], "images": [{"id": 153135281, "file_name": "Cyanistes_caeruleus_137402016_234664642.jpg", "width": 1920, "height": 1280}], "categories": [{"id": 8, "name": "Cyanistes_caeruleus"}]}                                   |
| https://inaturalist-open-data.s3.amazonaws.com/photos/203530620/original.jpg | (c) carabus123, some rights reserved (CC BY)   | fcc6f7b4004f388292bb27aa26f7e092 | {"annotations": [{"id": 161793985001, "image_id": 161793985, "category_id": 21, "bbox": [528.0, 385.0, 395.0, 368.00000000000006], "area": 145360.00000000003, "iscrowd": 0}], "images": [{"id": 161793985, "file_name": "Phoenicurus_phoenicurus_120343563_203530620.jpg", "width": 2048, "height": 1536}], "categories": [{"id": 21, "name": "Phoenicurus_phoenicurus"}]} |
| https://inaturalist-open-data.s3.amazonaws.com/photos/283444195/original.jpg | (c) bigben747400, some rights reserved (CC BY) | ca7b7c6459b29c36924bf02b09fb81a9 | {"annotations": [{"id": 153139593001, "image_id": 153139593, "category_id": 24, "bbox": [735.0, 399.0, 708.0, 334.0], "area": 236472.0, "iscrowd": 0}], "images": [{"id": 153139593, "file_name": "Pica_pica_163852657_283444195.jpg", "width": 1718, "height": 1146}], "categories": [{"id": 24, "name": "Pica_pica"}]}                                                    |

---

## Acknowledgements

This project uses **Label Studio** – provided free through the Academic Program by HumanSignal, Inc.  
[![Label Studio Logo](https://user-images.githubusercontent.com/12534576/192582340-4c9e4401-1fe6-4dbb-95bb-fdbba5493f61.png)](https://labelstud.io)

---
