# WatchMyBirds-Data

This dataset (11168 annotated images) is designed to train the models behind [**WatchMyBirds**](https://github.com/arminfabritzek/WatchMyBirds) – a lightweight, customizable object detection system tailored for real-time monitoring. Built with PyTorch and TensorFlow, WatchMyBirds supports live video streaming, automatic frame capture based on detection criteria, and Telegram integration for timely notifications. Images in the dataset may contain different species, and all annotations are provided in COCO format.

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

| original_url                                                                 | attribution                                              | image_hash                       | approved_annotation                                                                                                                                                                                                                                                                                                                            |
|:-----------------------------------------------------------------------------|:---------------------------------------------------------|:---------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| https://inaturalist-open-data.s3.amazonaws.com/photos/85866811/original.jpeg | (c) Alexis Tinker-Tsavalas, some rights reserved (CC BY) | 1677b2407d3651a4b97685dec2e90721 | {"annotations": [{"id": 153137821001, "image_id": 153137821, "category_id": 7, "bbox": [907.0, 552.0, 905.0, 857.0], "area": 775585.0, "iscrowd": 0}], "images": [{"id": 153137821, "file_name": "Columba_palumbus_53978688_85866811.jpeg", "width": 2048, "height": 1537}], "categories": [{"id": 7, "name": "Columba_palumbus"}]}            |
| https://inaturalist-open-data.s3.amazonaws.com/photos/454155570/original.jpg | (c) Iridescence, some rights reserved (CC BY-NC)         | 7852dd244ff48958e0b5300ba83d7065 | {"annotations": [{"id": 163032802001, "image_id": 163032802, "category_id": 4, "bbox": [518.0, 638.0, 310.0, 876.0], "area": 271560.0, "iscrowd": 0}], "images": [{"id": 163032802, "file_name": "Certhia_brachydactyla_253618936_454155570.jpg", "width": 1365, "height": 2048}], "categories": [{"id": 4, "name": "Certhia_brachydactyla"}]} |
| https://inaturalist-open-data.s3.amazonaws.com/photos/38787148/original.jpeg | (c) Alexis Tinker-Tsavalas, some rights reserved (CC BY) | 1f85004f27391eca8a1b3601bcc63d58 | {"annotations": [{"id": 153136414001, "image_id": 153136414, "category_id": 12, "bbox": [1042.0, 575.0, 324.0, 246.0], "area": 79704.0, "iscrowd": 0}], "images": [{"id": 153136414, "file_name": "Fringilla_coelebs_25065165_38787148.jpeg", "width": 2048, "height": 1538}], "categories": [{"id": 12, "name": "Fringilla_coelebs"}]}        |

---

## Acknowledgements

This project uses **Label Studio** – provided free through the Academic Program by HumanSignal, Inc.  
[![Label Studio Logo](https://user-images.githubusercontent.com/12534576/192582340-4c9e4401-1fe6-4dbb-95bb-fdbba5493f61.png)](https://labelstud.io)

---
