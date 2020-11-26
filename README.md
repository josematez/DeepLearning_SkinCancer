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

#### Conclusions and final comments


