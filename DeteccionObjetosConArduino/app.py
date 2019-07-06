import os
import time

import cv2
import serial


def guardarImagenObjeto(imagen):
    pathHaarcascade = "models/palomas.xml"
    pathSalida = "output/"

    clasificador = cv2.CascadeClassifier(pathHaarcascade)

    detectado = clasificador.detectMultiScale(
        imagen,
        minNeighbors=90,
        scaleFactor=3.5,
        minSize=(90,90)
    )

    if len(detectado) >= 1:
        for (x, y, w, h) in detectado:
            cv2.rectangle(imagen, (x, y), (x + w, y + h), (500, 600, 10), 3)
        pathSalida = pathSalida +str(len(os.listdir(path=pathSalida))+1)+".jpg"
        cv2.imwrite(pathSalida, imagen)
        comunicacionSerial.write(b'2')
        print("Reconocido, guardado y enviado!")

    del clasificador, imagen




captura = cv2.VideoCapture(0)
comunicacionSerial = serial.Serial('COM5', 9600)
while True:
    leido = comunicacionSerial.readline().decode("utf-8").rstrip("\r\n")
    if leido == "M":
        print("Movimiento Naranja!")

        a, capturado = captura.read()
        guardarImagenObjeto(capturado)
        time.sleep(2)

    del leido
captura.release()
cv2.destroyAllWindows()
comunicacionSerial.close()

