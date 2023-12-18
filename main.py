import torch
import cv2
import numpy as np
import pandas

# Leer el modelo
model = torch.hub.load('ultralytics/yolov5','custom',
                       path = 'C:/Users/HP/PycharmProjects/TopicosSelectosEnIAPrimerParcial/autos.pt')

cap = cv2.VideoCapture(0)

while True:

    # Lectura de la VideoCaptura
    ret, frame = cap.read()

    # Realizar deteccion
    detect = model(frame)

    info = detect.pandas().xyxy[0]
    print(info)

    # Mostrar FPS
    cv2.imshow('Detector de autos', np.squeeze(detect.render()))

    # Leer teclado
    t = cv2.waitKey(5)
    if t == 27:
        break

cap.release()
cv2.destroyAllWindows()
