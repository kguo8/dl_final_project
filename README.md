# Page Layout Analysis using Europeana Newspaper Dataset

The goal of the project is to replicate the text segmentation part as described in the following research paper

https://link.springer.com/article/10.1007/s00521-020-04910-x

The paper described using either U-Net Architecture or the modified U-Net(Wick) for this task. We implemented the Modified U-Net(Wick) Architecture for this task.

Preprocessing part was mostly generating the masks for the document images which were given in xml format.

The Modified U-Net wick model is stored in the wick_unet.py file.

Experiments conducted to improve the accuracy of the prediction were transforming the images using Albumentations package.Transformtions like PadIfNeeded, ShiftScaleRotate, RGBShift, RandomBrightnessContrast, Normalization were used.
