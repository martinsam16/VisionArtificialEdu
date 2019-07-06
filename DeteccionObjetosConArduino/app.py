import os
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
        return True


captura = cv2.VideoCapture(0)
comunicacionSerial = serial.Serial(port='COM5',baudrate=9600, timeout=1)
while True:
    a, capturado = captura.read()
    if a == True:
        leido = comunicacionSerial.readline().decode("utf-8").rstrip("\r\n")
        if leido == "M":
            print("Movimiento Naranja!")
            if guardarImagenObjeto(capturado) == True:
                comunicacionSerial.write(b'2')
                print("Enviado..")
        cv2.imshow('salida', capturado)
    else:
        break

    if cv2.waitKey(1) == ord('s'):
        break
    del leido


captura.release()
cv2.destroyAllWindows()
comunicacionSerial.close()

