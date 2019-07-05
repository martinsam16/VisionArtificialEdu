import os

import cv2
import serial

#Configuración serial
comunicacionSerial = serial.Serial(
    port='COM4',
    baudrate=9600,
    timeout=1
)


def guardarImagenObjeto(imagen):
    pathHaarcascade = "models/palomas.xml"
    pathSalida = "output/"

    clasificador = cv2.CascadeClassifier(pathHaarcascade)

    detectado = clasificador.detectMultiScale(
        imagen,
        minNeighbors=60,
        scaleFactor=3.5,
        minSize=(90,90),
        flags=cv2.CALIB_CB_NORMALIZE_IMAGE
    )

    if len(detectado) >= 1:
        for (x, y, w, h) in detectado:
            cv2.rectangle(imagen, (x, y), (x + w, y + h), (500, 600, 10), 3)
        pathSalida = pathSalida +str(len(os.listdir(path=pathSalida))+1)+".jpg"
        cv2.imwrite(pathSalida, imagen)
        comunicacionSerial.write(data=b'1')


    del clasificador, imagen


captura = cv2.VideoCapture(0)

while comunicacionSerial.is_open():
    leido = comunicacionSerial.read()
    print("Leido: ",leido)
    if not leido is None:
        for i in range (0,3):
            a, capturado = captura.read()

            if not a:
                break

            guardarImagenObjeto(capturado)

captura.release()
cv2.destroyAllWindows()
comunicacionSerial.close()

