# WatchMyBirds-Data

This dataset (9544 annotated images) is designed to train the models behind [**WatchMyBirds**](https://github.com/arminfabritzek/WatchMyBirds) – a lightweight, customizable object detection system tailored for real-time monitoring. Built with PyTorch and TensorFlow, WatchMyBirds supports live video streaming, automatic frame capture based on detection criteria, and Telegram integration for timely notifications. Images in the dataset may contain different species, and all annotations are provided in COCO format.

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

| original_url                                                                 | attribution                                              | image_hash                       | approved_annotation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:-----------------------------------------------------------------------------|:---------------------------------------------------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| https://inaturalist-open-data.s3.amazonaws.com/photos/468833721/original.png | (c) MurderSpagurder, some rights reserved (CC BY)        | 70477e3a3c6d80a7ec535814f8964673 | {"annotations": [{"id": 153138555001, "image_id": 153138555, "category_id": 5, "bbox": [298.84907834101375, 523.0434192672999, 192.91820276497754, 170.91044776119418], "area": 32971.73641584716, "iscrowd": 0}, {"id": 153138555002, "image_id": 153138555, "category_id": 5, "bbox": [732.8043205570089, 520.797483928143, 276.61485648744235, 144.77658941406906], "area": 40047.35550351408, "iscrowd": 0}], "images": [{"id": 153138555, "file_name": "Chloris_chloris_261012757_468833721.png", "width": 1327, "height": 1127}], "categories": [{"id": 5, "name": "Chloris_chloris"}]} |
| https://inaturalist-open-data.s3.amazonaws.com/photos/347327603/original.jpg | (c) Sem Khatov, some rights reserved (CC BY)             | 68ed54aa7c6f04fd215839fa218270a9 | {"annotations": [{"id": 153133922001, "image_id": 153133922, "category_id": 27, "bbox": [1005.0, 567.0, 331.0, 365.0], "area": 120815.0, "iscrowd": 0}], "images": [{"id": 153133922, "file_name": "Pyrrhula_pyrrhula_197233388_347327603.jpg", "width": 2048, "height": 1365}], "categories": [{"id": 27, "name": "Pyrrhula_pyrrhula"}]}                                                                                                                                                                                                                                                     |
| https://inaturalist-open-data.s3.amazonaws.com/photos/27246818/original.jpeg | (c) Alexis Tinker-Tsavalas, some rights reserved (CC BY) | a5d8cec36ba39caa45358ab11fa8b190 | {"annotations": [{"id": 153138319001, "image_id": 153138319, "category_id": 3, "bbox": [659.0, 397.0, 87.0, 153.0], "area": 13311.0, "iscrowd": 0}, {"id": 153138319002, "image_id": 153138319, "category_id": 3, "bbox": [589.0, 502.0, 81.0, 143.0], "area": 11583.0, "iscrowd": 0}], "images": [{"id": 153138319, "file_name": "Carduelis_carduelis_17849108_27246818.jpeg", "width": 1376, "height": 1032}], "categories": [{"id": 3, "name": "Carduelis_carduelis"}]}                                                                                                                    |

---

## Acknowledgements

This project uses **Label Studio** – provided free through the Academic Program by HumanSignal, Inc.  
[![Label Studio Logo](https://user-images.githubusercontent.com/12534576/192582340-4c9e4401-1fe6-4dbb-95bb-fdbba5493f61.png)](https://labelstud.io)

---
