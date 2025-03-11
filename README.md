# WatchMyBirds-Data

This dataset (8773 annotated images) is designed to train the models behind [**WatchMyBirds**](https://github.com/arminfabritzek/WatchMyBirds) – a lightweight, customizable object detection system tailored for real-time monitoring. Built with PyTorch and TensorFlow, WatchMyBirds supports live video streaming, automatic frame capture based on detection criteria, and Telegram integration for timely notifications. Images in the dataset may contain different species, and all annotations are provided in COCO format.

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

| original_url                                                                  | attribution                                              | image_hash                       | approved_annotation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:------------------------------------------------------------------------------|:---------------------------------------------------------|:---------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| https://inaturalist-open-data.s3.amazonaws.com/photos/175274103/original.jpeg | (c) carnifex, some rights reserved (CC BY)               | 8c2a7641bc56fd09d291ef21f4c92c06 | {"annotations": [{"id": 153140285001, "image_id": 153140285, "category_id": 10, "bbox": [1347.0, 904.0000000000001, 134.0, 255.0], "area": 34170.0, "iscrowd": 0}, {"id": 153140285002, "image_id": 153140285, "category_id": 11, "bbox": [606.0, 1003.0, 176.0, 178.0], "area": 31328.0, "iscrowd": 0}], "images": [{"id": 153140285, "file_name": "Emberiza_citrinella_104584708_175274103.jpeg", "width": 2048, "height": 1667}], "categories": [{"id": 10, "name": "Emberiza_citrinella"}, {"id": 11, "name": "Erithacus_rubecula"}]} |
| https://inaturalist-open-data.s3.amazonaws.com/photos/395659772/original.jpeg | (c) Bohan Jia, some rights reserved (CC BY)              | eed0ced2a525fab92b2894e82a68f73c | {"annotations": [{"id": 153138838001, "image_id": 153138838, "category_id": 12, "bbox": [858.0, 1157.0, 351.99999999999994, 344.0], "area": 121087.99999999999, "iscrowd": 0}], "images": [{"id": 153138838, "file_name": "Fringilla_coelebs_223308581_395659772.jpeg", "width": 1536, "height": 2048}], "categories": [{"id": 12, "name": "Fringilla_coelebs"}]}                                                                                                                                                                         |
| https://inaturalist-open-data.s3.amazonaws.com/photos/118567223/original.jpeg | (c) Alexis Tinker-Tsavalas, some rights reserved (CC BY) | 71a139698143f29f84d54cfa30c87d65 | {"annotations": [{"id": 153137159001, "image_id": 153137159, "category_id": 17, "bbox": [816.0, 369.99999999999994, 769.0, 892.0], "area": 685948.0, "iscrowd": 0}], "images": [{"id": 153137159, "file_name": "Passer_domesticus_72702940_118567223.jpeg", "width": 2048, "height": 1536}], "categories": [{"id": 17, "name": "Passer_domesticus"}]}                                                                                                                                                                                     |

---

## Acknowledgements

This project uses **Label Studio** – provided free through the Academic Program by HumanSignal, Inc.  
[![Label Studio Logo](https://user-images.githubusercontent.com/12534576/192582340-4c9e4401-1fe6-4dbb-95bb-fdbba5493f61.png)](https://labelstud.io)

---
