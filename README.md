![alt text](https://github.com/josematez/DeepLearning_SkinCancer/blob/main/label.png)
## Proyecto final del curso de Inteligencia artificial, impartido por Samsung Campus Innovation y la Univerdad de Malaga
## Participates:
+ Jose
+ Paula
+ Javier
+ Sergio
#### Decripcion del proyecto
+ El objetivo final del curso, consiste en contruir un modelo de inteligencia artificial, con la filosofia "Technology for Good", para solventar el problema del proyecto
elegido.
#### Eleccion del proyecto
+ Se extrajo de Kaggle un Dataset de HAM10mil imagenes con 7 clases diferentes entre benignas y malignas. Un problema de clasificacion multiclase.

Estando el contenido desbalanceado, y con una resolucion mayor de lo necesario, por lo que se aplico un redimensionando, a 75x100 pixeles, como también se aplico data augmentation, rotación, traslación ruido, etc, a las clases de menor tamaño para igualandolas a la clase de mayor numero de imagenes. Consiguiendo al final, 6000 mil imagenes por clase.

Las siguientes imagenes pertenecen al conjunto final utilizado para el entrenamiento de la red:

![alt text](https://github.com/sergioBSS/prueba/blob/main/ham.png)

#### Interfaz

Nuestra intención es contruir un modelo con la capacidad de distinguir entre las siete clases analizadas, con el fin de obtener un medio que permita con tan solo una imagen indicar con alta fiabilidad el tipo de patologia.

A fin de darle una aplicabilidad se contruyo esta interfaz de muy facil uso.

En la siguiente imagen se mostrara un ejemplo de su uso, para el cual se utilizo la imagen de un Dermatofibrona benigno.

![alt text](https://github.com/josematez/DeepLearning_SkinCancer/blob/main/CapturaBenigno.PNG)

Como se observa en la imagen se tiene dos botones "Choose Image" y "Scan", como también una breve descripción y recomendaciones debajo de la imagen seleccionada.

Choose Image : Usted selecciona la imagen a analizar del directorio en que se halle.

Scan : El modelo analiza la imagen.

Finalmente en el panel derecho, se tiene en la parte superior en color verde (benigno) la imagen predicha por el modelo y debajo todas las clases con la probabilidad asignada por la red, cuyos valores hace uso para determinar a que clase pertenece.

En la siguiente ejemplo se uso de una imagen de Melanoma de tipo maligna y es por ello que aparece el fondo de la parte superior del panel derecho en rojo.

![alt text](https://github.com/josematez/DeepLearning_SkinCancer/blob/main/CapturaMaligno.PNG)


