# WatchMyBirds-Data

This dataset (12062 annotated images) is designed to train the models behind [**WatchMyBirds**](https://github.com/arminfabritzek/WatchMyBirds) – a lightweight, customizable object detection system tailored for real-time monitoring. Built with PyTorch and TensorFlow, WatchMyBirds supports live video streaming, automatic frame capture based on detection criteria, and Telegram integration for timely notifications. Images in the dataset may contain different species, and all annotations are provided in COCO format.

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

| original_url                                                                  | attribution                                              | image_hash                       | approved_annotation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:------------------------------------------------------------------------------|:---------------------------------------------------------|:---------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| https://inaturalist-open-data.s3.amazonaws.com/photos/59968459/original.jpeg  | (c) Alexis Tinker-Tsavalas, some rights reserved (CC BY) | 080930a2018c82efd4689217cba72121 | {"annotations": [{"id": 153137263001, "image_id": 153137263, "category_id": 17, "bbox": [790.0, 431.0, 716.0, 984.0], "area": 704544.0, "iscrowd": 0}], "images": [{"id": 153137263, "file_name": "Passer_domesticus_37783422_59968459.jpeg", "width": 2048, "height": 1536}], "categories": [{"id": 17, "name": "Passer_domesticus"}]}                                                                                                                                                                                                                                                                                                                                                                                                                          |
| https://inaturalist-open-data.s3.amazonaws.com/photos/252417443/original.jpeg | (c) Niko Ioannidis, some rights reserved (CC BY)         | c03ff24bca4c21be1c6f5a6dd7b45514 | {"annotations": [{"id": 153140228001, "image_id": 153140228, "category_id": 10, "bbox": [219.0, 199.99999999999994, 170.0, 243.99999999999997], "area": 41479.99999999999, "iscrowd": 0}, {"id": 153140228002, "image_id": 153140228, "category_id": 10, "bbox": [438.99999999999994, 760.0, 111.00000000000001, 241.99999999999997], "area": 26862.0, "iscrowd": 0}, {"id": 153140228003, "image_id": 153140228, "category_id": 10, "bbox": [593.182732606874, 1.3099391217923633e-14, 147.20033528918685, 159.53072625698312], "area": 23482.9763939554, "iscrowd": 0}], "images": [{"id": 153140228, "file_name": "Emberiza_citrinella_146772219_252417443.jpeg", "width": 1600, "height": 1200}], "categories": [{"id": 10, "name": "Emberiza_citrinella"}]} |
| https://inaturalist-open-data.s3.amazonaws.com/photos/411732775/original.jpeg | (c) Alexis Tinker-Tsavalas, some rights reserved (CC BY) | 85fc87bf0b2f4f91e8ee82cfa858e289 | {"annotations": [{"id": 161793426001, "image_id": 161793426, "category_id": 25, "bbox": [1005.0, 294.99999999999994, 570.0, 1215.0], "area": 692550.0, "iscrowd": 0}], "images": [{"id": 161793426, "file_name": "Poecile_palustris_231793092_411732775.jpeg", "width": 2048, "height": 1536}], "categories": [{"id": 25, "name": "Poecile_palustris"}]}                                                                                                                                                                                                                                                                                                                                                                                                         |

---

## Acknowledgements

This project uses **Label Studio** – provided free through the Academic Program by HumanSignal, Inc.  
[![Label Studio Logo](https://user-images.githubusercontent.com/12534576/192582340-4c9e4401-1fe6-4dbb-95bb-fdbba5493f61.png)](https://labelstud.io)

---
