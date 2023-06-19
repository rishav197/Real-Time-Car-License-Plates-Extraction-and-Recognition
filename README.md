# Real Time Car License/Number Plates Extraction and Recognition
![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![OpenCV](https://img.shields.io/badge/OpenCV-red)
![EasyOCR](https://img.shields.io/badge/EasyOCR-fcba03)


<!-- Description -->
The project has been splitted up into two stages. The first stage is License/Number plate detection using the Haarcascade Classifier and generating samples. And the second stage is Recognition using the EasyOCR model. The Haarcascade classifier used for detecting car number plates from a live video feed captured through the webcam with the detected plate.
After detection, generated samples are further used for recognition using EasyOCR that provides optical character recognition functionality to extract text from detected/scanned samples of license/number plates.


## Detection using The Haar Cascade Model
The Haar Cascade classifier used for detecting car number plates from a live video feed captured by the webcam with detected plate.

It applies a minimum area threshold to detect car number plates and its value different for different country. for eg. it ranges from 2000-5000 sq pixels for the vehicles with indian registration number plates.

The Haarcascade classifier defined in a .xml file contains the model weights obtained during pre-training of model on vehicles with Indian registration number plates.


## Real Time Detection
