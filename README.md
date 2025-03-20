# WatchMyBirds-Data

This dataset (10556 annotated images) is designed to train the models behind [**WatchMyBirds**](https://github.com/arminfabritzek/WatchMyBirds) – a lightweight, customizable object detection system tailored for real-time monitoring. Built with PyTorch and TensorFlow, WatchMyBirds supports live video streaming, automatic frame capture based on detection criteria, and Telegram integration for timely notifications. Images in the dataset may contain different species, and all annotations are provided in COCO format.

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

| original_url                                                                  | attribution                                      | image_hash                       | approved_annotation                                                                                                                                                                                                                                                                                                                                                               |
|:------------------------------------------------------------------------------|:-------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| https://inaturalist-open-data.s3.amazonaws.com/photos/459501148/original.jpeg | (c) Anton Dangl, some rights reserved (CC BY-NC) | d13d02aa046bcad8a7dc88cf89ef67f8 | {"annotations": [{"id": 163032178001, "image_id": 163032178, "category_id": 4, "bbox": [883.0, 542.0, 181.0, 379.0], "area": 68599.0, "iscrowd": 0}], "images": [{"id": 163032178, "file_name": "Certhia_brachydactyla_256302163_459501148.jpeg", "width": 2048, "height": 1365}], "categories": [{"id": 4, "name": "Certhia_brachydactyla"}]}                                    |
| https://inaturalist-open-data.s3.amazonaws.com/photos/146565989/original.jpg  | (c) richyfourtytwo, some rights reserved (CC BY) | 8fdf0bf0b150c2d1ad7e3403c1c2a62f | {"annotations": [{"id": 153136580001, "image_id": 153136580, "category_id": 9, "bbox": [129.0, 155.0, 177.99999999999997, 251.0], "area": 44677.99999999999, "iscrowd": 0}], "images": [{"id": 153136580, "file_name": "Dendrocopos_major_88801294_146565989.jpg", "width": 478, "height": 444}], "categories": [{"id": 9, "name": "Dendrocopos_major"}]}                         |
| https://inaturalist-open-data.s3.amazonaws.com/photos/214320162/original.jpeg | (c) joba102, some rights reserved (CC BY)        | a55c4518f256253893b7bfc8d108759b | {"annotations": [{"id": 161795440001, "image_id": 161795440, "category_id": 4, "bbox": [938.0, 583.9999999999999, 270.0, 326.00000000000006], "area": 88020.00000000001, "iscrowd": 0}], "images": [{"id": 161795440, "file_name": "Certhia_brachydactyla_126320252_214320162.jpeg", "width": 2048, "height": 1536}], "categories": [{"id": 4, "name": "Certhia_brachydactyla"}]} |

---

## Acknowledgements

This project uses **Label Studio** – provided free through the Academic Program by HumanSignal, Inc.  
[![Label Studio Logo](https://user-images.githubusercontent.com/12534576/192582340-4c9e4401-1fe6-4dbb-95bb-fdbba5493f61.png)](https://labelstud.io)

---
