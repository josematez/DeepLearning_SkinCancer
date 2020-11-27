# -*- coding: utf-8 -*-
"""
SkinScan
"""

# Libraries
import tkinter as tk
import deepdish as dd
import cv2
from PIL import ImageTk, Image
from tkinter import filedialog
import numpy as np
import tensorflow as tf
import keras
import os
import h5py
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

os.chdir('D:/javier/Escritorio/PYTHON/Curso_IA_Samsung/Proyecto')



############## Funtions ##############

# load_img() Load the image to classify and shows it in a Label

def load_img():
    
    global img, image_data
    for img_display in canvas1.winfo_children():
        img_display.destroy()

    image_data = filedialog.askopenfilename(initialdir="/", title="Choose an image",
                                            filetypes=(("all files", "*.*"), 
                                                       ("png files", "*.png"), 
                                                       ("jpg files", "*.jpg"), 
                                                       ("jpeg files", "*.jpeg")))
    basewidth = 400
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel_image = tk.Label(canvas1, image=img).pack()

# classify() Scan and classify the image

def classify(model, classes):
    
    # Clean the content in the canvas when excecute the function
    for text in canvas2.winfo_children():
        text.destroy()
    for tipo in canvas3.winfo_children():
        tipo.destroy()
        
    # Dictionary that contains the name and information about each class of lesion
    dic  = {'Actinic Keratosis': """Actinic Keratosis: \nIt is a thick, scaly patch on the skin that develops after many years 
            of sun exposure, with the possibility of turning into cancer. To reduce risk, minimize your sun exposure and protect 
            your skin from UV rays.""",
            
            'Basal Cell Carcinoma': """Basal Cell Carcinoma: \nA type of skin cancer that occurs in the basal cells, it is due to the 
            mutation of their DNA caused by ultraviolet radiation. Avoiding prolonged periods of exposure to this type of radiation 
            such as sunlight or tanning lamps can be ways to protect yourself against the basal cell carcinoma.""",
            
            'Benign Keratosis-Like Lesion': """Benign Keratosis-Like Lesion:\nThese are benign moles that occur with aging, 
            they can appear on the back or chest, but can occur anywhere on the body. It grows slowly, in groups or individually. 
            Most people will develop at least one in their entire life.""",
            
            'Dermatofibroma': """Dermatofibroma: \nSlow-growing benign tumor of various morphologies and size between 0.5 to 2cm and a 
            hard consistency. They can be yellowish or grayish brown. Its exact causes are unknown, but it is a tumor that has no risk 
            of becoming malignant. Usually, in most cases, there is only one injury.""",
            
            'Melanocytic Nevi': """Melanocytic Nevi: \nPigmented spot that is colloquially called mole. It is a benign tumor, 
            commonly brown in color, it can also be bluish-red, etc. They are nevi that require a medical diagnosis, as they 
            could lead to cancer with aging""",
            
            'Melanoma': """Melanoma: \nA type of skin cancer that occurs in melanocytes that make melanin, the pigment that 
            gives skin its color. The exact cause of all melanomas is not clear, but exposure to UV radiation increases the risk 
            of having it. The risk of developing melanoma appears to be increased in people under 40 years of age, especially women. 
            Melanoma can be treated successfully if caught early.""",
            
            'Vascular Lesions': """Vascular Lesions: \nThey are abnormally dense accumulations of blood or lymphatic vessels, which are 
            located on the skin or underneath, producing abnormalities of reddish or purple color. The malformations and bulges of the 
            vessels can be: hemangiomas, lymphangiomas, pyogenic granulomas, spider veins and Port wine stains."""}
            
    # Processes the entered image to work with the model
    image = np.asarray(Image.open(image_data).resize((100, 75))).reshape(-1, 75, 100, 3)
    image = image / np.max(image)

    class_probs = [np.round(prob * 100.0, 2) for prob in model.predict(image)[0]]
    class_idx = np.argmax(class_probs)

    # Shows the probabilistic result of each class
    for i in range(len(classes)):
        result = tk.Label(canvas2, bg="white", font=("", 14), anchor='w',
                          text='- ' + classes[i] + ': ' + str(class_probs[i]) + 
                          '%').pack(fill=tk.BOTH, padx=10, pady=10, expand=1)
    
    # Shows the class with the highest probability obtained and modifies the color depending on whether it is malignant or benign
    if classes[class_idx]=="Actinic Keratosis":
        tk.Label(canvas3, bg="green", text="Actinic Keratosis (Benign)", font=("", 14, 'bold')).pack(fill=tk.BOTH, padx=4, pady=4, expand=1)
        info_label.config(text=dic["Actinic Keratosis"])
    elif classes[class_idx]=="Basal Cell Carcinoma":
        tk.Label(canvas3, bg="red", text="Basal Cell Carcinoma (Malign)", font=("", 14, 'bold')).pack(fill=tk.BOTH, padx=4, pady=4, expand=1)
        info_label.config(text=dic["Basal Cell Carcinoma"])
    elif classes[class_idx]=="Benign Keratosis-Like Lesion":
        tk.Label(canvas3, bg="green", text="Keratosis-Like Lesion (Benign)", font=("", 14, 'bold')).pack(fill=tk.BOTH, padx=4, pady=4, expand=1)
        info_label.config(text=dic["Benign Keratosis-Like Lesion"])
    elif classes[class_idx]=="Dermatofibroma":
        tk.Label(canvas3, bg="green", text="Dermatofibroma (Benign)", font=("", 14, 'bold')).pack(fill=tk.BOTH, padx=4, pady=4, expand=1)
        info_label.config(text=dic["Dermatofibroma"])
    elif classes[class_idx]=="Melanocytic Nevi":
        tk.Label(canvas3, bg="green", text="Melanocytic Nevi (Benign)", font=("", 14, 'bold')).pack(fill=tk.BOTH, padx=4, pady=4, expand=1)
        info_label.config(text=dic["Melanocytic Nevi"])
    elif classes[class_idx]=="Melanoma":
        tk.Label(canvas3, bg="red", text="Melanoma (Malign)", font=("", 14, 'bold')).pack(fill=tk.BOTH, padx=4, pady=4, expand=1)
        info_label.config(text=dic["Melanoma"])
    elif classes[class_idx]=="Vascular Lesions":
        tk.Label(canvas3, bg="red", text="Vascular Lesions (Malign)", font=("", 14, 'bold')).pack(fill=tk.BOTH, padx=4, pady=4, expand=1)
        info_label.config(text=dic["Vascular Lesions"])
        

# window_about() Open a new window in the about section
def window_about():
    newWindow = tk.Toplevel(root)
    newWindow.title("About SkinScan")
    newWindow.geometry("500x350") # Window size
    newWindow.resizable(0, 0) # No resize
    newWindow.iconbitmap('./Logo.ico')
    
    body="""This program has been developed like a project for the \"Artificial Intelligence\" course taught in collaboration with 
    Samsung Innovation Campus and The Málaga University. \n\nThe SkinScan objective is to indicate through the photograph of a mole, 
    whether it is malignant or benign and to categorize it among 7 different types of pathologies, to this, Deep Neural Networks and 
    Deep Learning Techniques have been used"""
    
    authors='Authors:\nJavier Espinosa Montosa \nJosé Luis Matez Bandera \nPaula Ruiz Barroso \nSergio Boggero Suaznabar'
    
    body_label = tk.Label(newWindow, text=body, font=("", 12), wraplength=450, justify=tk.LEFT).place(relx=0.02, rely=0.057, height=150, width=464)
    
    authors_label = tk.Label(newWindow, text=authors, font=("", 12), wraplength=450, justify=tk.LEFT).place(relx=0.02, rely=0.514, height=151, width=204)
    
    logo_image = ImageTk.PhotoImage(Image.open("./Logo2.ico"))
    
    logo_frame = tk.Label(newWindow, image=logo_image).place(relx=0.58, rely=0.520)
    
    newWindow.mainloop()
    
############## GUI ##############

root = tk.Tk() # Start of the GUI loop
root.iconbitmap('./Logo.ico')
root.resizable(1,  1)
root.geometry("1280x720") # Initial size
root.minsize(1280, 720) # Minimum size when resize the window
root.maxsize(3124, 1031) # Max size when resize the window
root.title("SkinScan")
root.configure(background="#d9d9d9") 

# Menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
menubar.add_cascade(label="SkinScan", menu=file_menu)
file_menu.add_command(label="New file", command=load_img) # Choose and load and image form your computer
file_menu.add_command(label="About SkinScan", command=window_about) # Shows a pop-up window with information about the program
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy) # Close the program

# GUI body

# Title in the top
title = tk.Label(root, text="SkinScan: control your skin with AI", 
               bg="#193EB0", fg="white", padx=1000, pady=6,font=("", 12)).pack()

# The place where the uploaded image is displayed
canvas1 = tk.Canvas(root)
canvas1.place(relx=0.067, rely=0.130, relheight=0.608, relwidth=0.499)
canvas1.config(bg="#d9d9d9", relief="ridge", highlightbackground="#d9d9d9")

# The place where the probabilistic results are showed
canvas2 = tk.Canvas(root)
canvas2.place(relx=0.612, rely=0.240, relheight=0.700, relwidth=0.329)
canvas2.config(bg="white", borderwidth=2, relief="ridge")

# The place where the most probable injury appears
canvas3 = tk.Canvas(root)
canvas3.place(relx=0.612, rely=0.130, relheight=0.1, relwidth=0.329)
canvas3.config(bg="#d9d9d9", borderwidth=2, relief="ridge")

# This label shows a brief information about the lesion predicted
info_label = tk.Label(root, wraplength=550)
info_label.place(relx=0.067, rely=0.550, relheight=0.22, relwidth=0.479)
info_label.config(bg="#d9d9d9", relief="flat", font=("", 13), justify=tk.LEFT)

# Buttons

# This button calls the load_img() function and allows you to choose a photo from your computer to classify.
choose_image = tk.Button(root, text='Choose Image', command=load_img)
choose_image.place(relx=0.065, rely=0.848, height=44, width=97)
choose_image.config(pady="0", bg="Grey")

# This button calls the classify() function, which will classify the image through the model
class_image = tk.Button(root, text='Scan', command=lambda: classify(model, classes))
class_image.place(relx=0.461, rely=0.85, height=44, width=107)
class_image.config(pady="0", bg="Grey")

############## Densenet Model ##############
classes = ['Actinic Keratosis', 'Basal Cell Carcinoma', 'Benign Keratosis-Like Lesion', 'Dermatofibroma',
           'Melanocytic Nevi', 'Melanoma', 'Vascular Lesions']

n_classes = 7
input_shape = (75, 100, 3)

densenet = tf.keras.applications.DenseNet201(weights='imagenet', include_top=False, input_shape=input_shape)

model = tf.keras.models.Sequential()
model.add(densenet)
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dropout(0.25))
model.add(tf.keras.layers.Dense(512, activation='relu'))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.46))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.46))
model.add(tf.keras.layers.Dense(n_classes, activation='softmax'))

# ----- WEIGHTS
model.load_weights('./models/densenet_weights.hdf5') # Load the trained weights
print('[INFO] Model loaded correctly!')

root.mainloop() # End of the GUI loop