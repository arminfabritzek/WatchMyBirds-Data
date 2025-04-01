# WatchMyBirds-Data

This dataset (13522 annotated images) is designed to train the models behind [**WatchMyBirds**](https://github.com/arminfabritzek/WatchMyBirds) – a lightweight, customizable object detection system tailored for real-time monitoring. Built with PyTorch and TensorFlow, WatchMyBirds supports live video streaming, automatic frame capture based on detection criteria, and Telegram integration for timely notifications. Images in the dataset may contain different species, and all annotations are provided in COCO format.

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

| original_url                                                                  | attribution                                              | image_hash                       | approved_annotation                                                                                                                                                                                                                                                                                                                                           |
|:------------------------------------------------------------------------------|:---------------------------------------------------------|:---------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| https://inaturalist-open-data.s3.amazonaws.com/photos/32135676/original.jpeg  | (c) Alexis Tinker-Tsavalas, some rights reserved (CC BY) | be517d4f3c15ad510b41bcc9fa56ef1a | {"annotations": [{"id": 161795769001, "image_id": 161795769, "category_id": 6, "bbox": [825.0, 738.0, 286.0, 467.0], "area": 133562.0, "iscrowd": 0}], "images": [{"id": 161795769, "file_name": "Coccothraustes_coccothraustes_20833913_32135676.jpeg", "width": 2048, "height": 1536}], "categories": [{"id": 6, "name": "Coccothraustes_coccothraustes"}]} |
| https://inaturalist-open-data.s3.amazonaws.com/photos/59887365/original.jpeg  | (c) Alexis Tinker-Tsavalas, some rights reserved (CC BY) | 8d3392d00f11d775cc5c77997e69d1f4 | {"annotations": [{"id": 153137265001, "image_id": 153137265, "category_id": 17, "bbox": [618.0, 419.0, 225.0, 152.0], "area": 34200.0, "iscrowd": 0}], "images": [{"id": 153137265, "file_name": "Passer_domesticus_37738585_59887365.jpeg", "width": 1236, "height": 927}], "categories": [{"id": 17, "name": "Passer_domesticus"}]}                         |
| https://inaturalist-open-data.s3.amazonaws.com/photos/351086574/original.jpeg | (c) Valentin Conrad, some rights reserved (CC BY)        | ddc9c1a4344d408240294b325239d767 | {"annotations": [{"id": 153139208001, "image_id": 153139208, "category_id": 14, "bbox": [1136.0, 525.0, 249.0, 273.0], "area": 67977.0, "iscrowd": 0}], "images": [{"id": 153139208, "file_name": "Garrulus_glandarius_199116353_351086574.jpeg", "width": 2048, "height": 1536}], "categories": [{"id": 14, "name": "Garrulus_glandarius"}]}                 |

---

## Acknowledgements

This project uses **Label Studio** – provided free through the Academic Program by HumanSignal, Inc.  
[![Label Studio Logo](https://user-images.githubusercontent.com/12534576/192582340-4c9e4401-1fe6-4dbb-95bb-fdbba5493f61.png)](https://labelstud.io)

---
