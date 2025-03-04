# WatchMyBirds-Data

This dataset (4788 annotated images) is designed to train the models behind [**WatchMyBirds**](https://github.com/arminfabritzek/WatchMyBirds) – a lightweight, customizable object detection system tailored for real-time monitoring. Built with PyTorch and TensorFlow, WatchMyBirds supports live video streaming, automatic frame capture based on detection criteria, and Telegram integration for timely notifications. Images in the dataset may contain different species, and all annotations are provided in COCO format.

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

| original_url                                                                 | attribution                                              | image_hash                       | approved_annotation                                                                                                                                                                                                                                                                                                                                               |
|:-----------------------------------------------------------------------------|:---------------------------------------------------------|:---------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| https://inaturalist-open-data.s3.amazonaws.com/photos/57548688/original.jpeg | (c) Alexis Tinker-Tsavalas, some rights reserved (CC BY) | 41ef1303ee20d65c7afb0f6afda663a7 | {"annotations": [{"id": 153137559001, "image_id": 153137559, "category_id": 12, "bbox": [854.0, 577.9999999999999, 642.0, 857.0], "area": 550194.0, "iscrowd": 0}], "images": [{"id": 153137559, "file_name": "Parus_major_36408234_57548688.jpeg", "width": 2048, "height": 1536}], "categories": [{"id": 12, "name": "Parus_major"}]}                           |
| https://inaturalist-open-data.s3.amazonaws.com/photos/242991383/original.jpg | (c) Sem Khatov, some rights reserved (CC BY)             | e61ef38aace91fb4e47c6732441823d3 | {"annotations": [{"id": 153134561001, "image_id": 153134561, "category_id": 12, "bbox": [403.0, 572.0, 428.0, 219.99999999999997], "area": 94159.99999999999, "iscrowd": 0}], "images": [{"id": 153134561, "file_name": "Parus_major_141794403_242991383.jpg", "width": 2048, "height": 1365}], "categories": [{"id": 12, "name": "Parus_major"}]}                |
| https://inaturalist-open-data.s3.amazonaws.com/photos/465752340/original.jpg | (c) Andrea, some rights reserved (CC BY)                 | dc4ab8244c05bdeb937e012dc090a4c8 | {"annotations": [{"id": 153139086001, "image_id": 153139086, "category_id": 10, "bbox": [455.0, 351.0, 862.0, 940.9999999999999], "area": 811141.9999999999, "iscrowd": 0}], "images": [{"id": 153139086, "file_name": "Garrulus_glandarius_259458432_465752340.jpg", "width": 2048, "height": 1618}], "categories": [{"id": 10, "name": "Garrulus_glandarius"}]} |
