## Page Layout Analysis using Europeana Newspapers Dataset

### Table of Contents
-----
* [Goal of the Project](https://github.com/kguo8/dl_final_project#goal-of-the-project)
* [Dataset](https://github.com/kguo8/dl_final_project#dataset)
* [Model Architecture](https://github.com/kguo8/dl_final_project#model-architecture)
* [Experiments](https://github.com/kguo8/dl_final_project#experiments)
* [Results](https://github.com/kguo8/dl_final_project#results)
* [Future Steps](https://github.com/kguo8/dl_final_project#future-steps)
* [Technologies](https://github.com/kguo8/dl_final_project#technologies)
* [References](https://github.com/kguo8/dl_final_project#references)

### Goal of the Project
-----

The goal of the project is to experiment with using a modified U-Net to perform layout segmentation on historical documents. We are doing this with the help of the research paper below:

[Building an efficient OCR system for historical documents with little training data](https://link.springer.com/article/10.1007/s00521-020-04910-x)

### Dataset 
---

The Dataset used for this project is the [Europeana  Project Dataset](https://ieeexplore.ieee.org/document/7333898), which contains 500+ pages newspaper scans with ground truths containing layout information. For this project, we focused on the English Dataset with 50 images

Data Pre-processing part was mostly generating the masks for the document images which were in the xml format.

### Model Architecture
---

We used the Modified U-Net Architecture as proposed in [Fully Convolutional Neural Networks for Page Segmentation of Historical Document Images](https://arxiv.org/abs/1711.07695)  paper.It’s different from a traditional U-Net in a way that it does not use any skip connections and it has fewer convolution layers. So, this version is much quicker to run than a more traditional U-Net architecture.

The pytorch implementation of model architecture could be found [here](https://github.com/kguo8/dl_final_project/blob/main/wick_unet.py)

### Experiments
---

We conducted 3 experiments, as described below, on the training set to check which Image Augmentations were best using the [Albumentations](https://github.com/albumentations-team/albumentations) library. 

* Padding + Resizing
* Padding + Resizing + ShiftScaleRotate + RGBShift+ RandomBrightnessContrast
* Padding + Resizing + Rotation + GaussNoise

We padded the images to two-thirds ratio and we resized it to 390 * 260 for quicker computation time.

The experiments can be found [here](https://github.com/kguo8/dl_final_project/tree/main/experiments)

### Results
---

We found that the model trained with third experiment performed best on the validation set. So, we used this on the test set and got an F1 score of 0.31.

### Future Steps
---

* Use more training data.
* Experiment with padding dynamically instead of padding to maximum image size.

### Technologies
---
* Pytorch v1.7
* Python v3.8


### References
---
* [Building an efficient OCR system for historical documents with little training data](https://link.springer.com/article/10.1007/s00521-020-04910-x)
* [Europeana  Project Dataset](https://ieeexplore.ieee.org/document/7333898)
* [Fully Convolutional Neural Networks for Page Segmentation of Historical Document Images](https://arxiv.org/abs/1711.07695)

