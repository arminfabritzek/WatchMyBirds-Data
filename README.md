# WatchMyBirds-Data

This dataset (7526 annotated images) is designed to train the models behind [**WatchMyBirds**](https://github.com/arminfabritzek/WatchMyBirds) – a lightweight, customizable object detection system tailored for real-time monitoring. Built with PyTorch and TensorFlow, WatchMyBirds supports live video streaming, automatic frame capture based on detection criteria, and Telegram integration for timely notifications. Images in the dataset may contain different species, and all annotations are provided in COCO format.

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

| original_url                                                                  | attribution                                              | image_hash                       | approved_annotation                                                                                                                                                                                                                                                                                                                                                            |
|:------------------------------------------------------------------------------|:---------------------------------------------------------|:---------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| https://inaturalist-open-data.s3.amazonaws.com/photos/121303287/original.jpeg | (c) Lennart Hudel, some rights reserved (CC BY)          | 64514926a2a1859e97588142873d1e7f | {"annotations": [{"id": 153140363001, "image_id": 153140363, "category_id": 10, "bbox": [945.0, 535.0000000000001, 281.0, 206.99999999999997], "area": 58166.99999999999, "iscrowd": 0}], "images": [{"id": 153140363, "file_name": "Emberiza_citrinella_74233629_121303287.jpeg", "width": 2048, "height": 1365}], "categories": [{"id": 10, "name": "Emberiza_citrinella"}]} |
| https://inaturalist-open-data.s3.amazonaws.com/photos/30433825/original.jpeg  | (c) Alexis Tinker-Tsavalas, some rights reserved (CC BY) | 5bc081e2c4ecee17c42f2f9608e450d6 | {"annotations": [{"id": 153137674001, "image_id": 153137674, "category_id": 16, "bbox": [900.0, 691.9999999999999, 199.0, 184.00000000000003], "area": 36616.00000000001, "iscrowd": 0}], "images": [{"id": 153137674, "file_name": "Parus_major_19751616_30433825.jpeg", "width": 2048, "height": 1536}], "categories": [{"id": 16, "name": "Parus_major"}]}                  |
| https://inaturalist-open-data.s3.amazonaws.com/photos/112015704/original.jpeg | (c) joba102, some rights reserved (CC BY)                | 9880881fe686971c872a9b9592448c7a | {"annotations": [{"id": 153140661001, "image_id": 153140661, "category_id": 5, "bbox": [1014.0, 501.0, 169.0, 162.0], "area": 27378.0, "iscrowd": 0}], "images": [{"id": 153140661, "file_name": "Chloris_chloris_69082449_112015704.jpeg", "width": 2048, "height": 1536}], "categories": [{"id": 5, "name": "Chloris_chloris"}]}                                             |

---

## Acknowledgements

This project uses **Label Studio** – provided free through the Academic Program by HumanSignal, Inc.  
[![Label Studio Logo](https://user-images.githubusercontent.com/12534576/192582340-4c9e4401-1fe6-4dbb-95bb-fdbba5493f61.png)](https://labelstud.io)

---
