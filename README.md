## TopicosSelectosEnIAPrimerParcial

- Natalia Bilbao Cano
- Código: 40987
- Ingenieria de Sistemas Computacionales
- 8vo Semestre

# YOLOv5 Object Detection Model

Este repositorio contiene un modelo de detección de objetos en tiempo real entrenado con YOLOv5, utilizando la documentación proporcionada en el cuaderno de Google Colab `YOLOv5-Custom-Training.ipynb`. El modelo ha sido entrenado con un conjunto de datos personalizado para detectar objetos específicos.

## ¿Que es la detección de objetos?

Es un campo clave de la Inteligencia Artificial que implica redes neuronales convolucionales, este permite a los sistemas informáticos "ver" su entorno y detectar objetos en imagenes  o fotogramas.

## Requistos del Modelo de Detección 

1. El modelo deberá detectar multiples objetos, deberá detectar al menos 1 clase.
2. Deberá entregar la posición en el espacio del objeto y deberá tener la posibilidad de realiazar la inferencia en tiempo real.

## Procedimiento

1. Crear Dataset
   - Almacenar un conjunto de imagenes del objeto que queremos detectar.
   - Etiquetar las imagenes señalando el objeto a dectar.
2. Entrenamiento
   Medianate YOLOv5
3. Inferencia
   Poner en practica lo que nuestra red neuronal aprendio luego del entrenamiento, para este proyecto se hara en tiempo real.

## Cómo ejecutar el programa en PyCharm

1. Tener instaldo Python version 9 o 10
2. Abrir la terminal y ejecutar el siguiente comando para instalar los paquetes necesarios (pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt)
3. Una vez termine la instalacion hacer correr el archivo main.py

## Links usados para este proyecto

YOLOv5 (https://github.com/ultralytics/yolov5). 

Notebook Google Colab (https://colab.research.google.com/github/roboflow-ai/yolov5-custom-training-tutorial/blob/main/yolov5-custom-training.ipynb#scrollTo=7iiObB2WCMh6)

Ultralytics YOLOv8 Docs (https://docs.ultralytics.com/yolov5/tutorials/pytorch_hub_model_loading/)


