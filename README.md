# WatchMyBirds-Data

This dataset (6689 annotated images) is designed to train the models behind [**WatchMyBirds**](https://github.com/arminfabritzek/WatchMyBirds) – a lightweight, customizable object detection system tailored for real-time monitoring. Built with PyTorch and TensorFlow, WatchMyBirds supports live video streaming, automatic frame capture based on detection criteria, and Telegram integration for timely notifications. Images in the dataset may contain different species, and all annotations are provided in COCO format.

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

| original_url                                                                  | attribution                                              | image_hash                       | approved_annotation                                                                                                                                                                                                                                                                                                                       |
|:------------------------------------------------------------------------------|:---------------------------------------------------------|:---------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| https://inaturalist-open-data.s3.amazonaws.com/photos/31610560/original.jpeg  | (c) Alexis Tinker-Tsavalas, some rights reserved (CC BY) | 58ad17c0cde93464f2e90f3bc12d90d6 | {"annotations": [{"id": 153134265001, "image_id": 153134265, "category_id": 19, "bbox": [935.0, 637.0, 225.0, 411.0], "area": 92475.0, "iscrowd": 0}], "images": [{"id": 153134265, "file_name": "Spinus_spinus_20483303_31610560.jpeg", "width": 1947, "height": 1460}], "categories": [{"id": 19, "name": "Spinus_spinus"}]}            |
| https://inaturalist-open-data.s3.amazonaws.com/photos/339723042/original.jpg  | (c) Oriol Sastre, some rights reserved (CC BY)           | 470d44f8e8c459c10d78186bde6d8e16 | {"annotations": [{"id": 153139221001, "image_id": 153139221, "category_id": 10, "bbox": [343.0, 365.0, 194.0, 151.0], "area": 29294.0, "iscrowd": 0}], "images": [{"id": 153139221, "file_name": "Garrulus_glandarius_193390529_339723042.jpg", "width": 854, "height": 854}], "categories": [{"id": 10, "name": "Garrulus_glandarius"}]} |
| https://inaturalist-open-data.s3.amazonaws.com/photos/286634537/original.jpeg | no rights reserved                                       | cfff2ec949caac1376c76c6ad3033723 | {"annotations": [{"id": 153141383001, "image_id": 153141383, "category_id": 18, "bbox": [924.0, 388.0, 326.0, 210.0], "area": 68460.0, "iscrowd": 0}], "images": [{"id": 153141383, "file_name": "Sitta_europaea_165583532_286634537.jpeg", "width": 2048, "height": 1365}], "categories": [{"id": 18, "name": "Sitta_europaea"}]}        |
