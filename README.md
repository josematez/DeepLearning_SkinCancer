![alt text](https://github.com/josematez/DeepLearning_SkinCancer/blob/main/Images/label.png)
## Final project of the Artificial Intelligence course, taught by Samsung Campus Innovation and the University of Malaga
## Participants:
+ José Luis Matez
+ Paula Ruiz Barroso
+ Javier Espinosa Montosa
+ Sergio Boggero Suaznabar

## Tutors:
+ Antonio Jesús Nebro Urbaneja
+ José Manuel Garcia Nieto

#### Project description
+ The final objective of the course is to build an artificial intelligence model, with the "Technology for Good" philosophy, to solve the problem of the chosen project.
#### Project choice
+ A Dataset of HAM10 thousand images with 7 different classes between benign and malignant was extracted from Kaggle. A multiclass classification problem.

Being the content unbalanced and with a higher resolution than necessary, so a resizing was applied, at 75x100 pixels, as well as data augmentation, rotation, translation, noise, etc., to the smaller classes to equalize them to the class with the largest number of images. Getting in the end, 3000 thousand images per class.

The following images belong to the final set used for the training of the network:

![alt text](https://github.com/josematez/DeepLearning_SkinCancer/blob/main/Images/ham.png)

## Interface:

Our intention is to build a model with the ability to distinguish between the seven classes analyzed, in order to obtain a means that allows, with just one image, to indicate the type of pathology with high reliability.

In order to give it applicability, this very easy-to-use interface was built.

In the following image an example of its use will be shown, for which the image of a benign Dermatofibrona was used.

![alt text](https://github.com/josematez/DeepLearning_SkinCancer/blob/main/Images/CapturaBenigno.PNG)

As can be seen in the image, there are two buttons "Choose Image" and "Scan", as well as a brief description and recommendations below the selected image.

Choose Image: You select the image to analyze from the directory in which it is located.

Scan: The model analyzes the image.

Finally, in the right panel, the image predicted by the model is in the upper part in green (benign) and below all the classes with the probability assigned by the network, whose values it uses to determine which class it belongs to.

In the following example an image of Melanoma was used and that is why the background at the top of the right panel appears in red.

![alt text](https://github.com/josematez/DeepLearning_SkinCancer/blob/main/Images/CapturaMaligno.PNG)

#### GUI Installation

You must download the folder with the source code and all necessary files for program execution through this link:

https://mega.nz/folder/Km4AASzS#lw48Ef1ODsk5kDrA2cNnBQ

You can run the source code(SkinScan.py) directly from a python shell or in a command prompt. You need to have the requisites in steps 1 and 2 installed in your enviroment or PC.

----------------------------------------------------------------------------

If you want to create an executable file for windows 10, follow these steps:

It is recommended to create a virtual environment with all dependencies.

STEPS:

1- Install Python 3.7 

2- libraries and necessary versions:

	- Tkinter 0.1.0
	- Deepdish 0.3.6
	- OpenCV 4.4.0.46
	- Pillow (PIL) 8.0.1
	- Numpy 1.18.5
	- Tensorflow 2.3.0
	- keras 2.3.0
	 -h5py 2.10.0

3- With a command prompt positioned in the root folder (The one with the source code and files), run the command below for build the .exe file. (pyinstaller 4.1 or higher is required in your enviroment or pc for this step)

	pyinstaller --onefile -w SkinScan.py

4- Once the program has compiled, copy or cut the executable contained in the 'dist' folder and paste it into the root folder and execute it.

#### Conclusions and final comments


