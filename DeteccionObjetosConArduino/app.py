import threading as hilo

import cv2
import numpy as np



def guardarImagenObjeto(img, contador):
    copia = np.array(img)
    pathHaarcascade = "models/palomas.xml"
    pathSalida = "output/"

    clasificador = cv2.CascadeClassifier(pathHaarcascade)

    detectado = clasificador.detectMultiScale(
        copia,
        minNeighbors=90,
        scaleFactor=3.5,
        minSize=(90,90)
    )

    if len(detectado) >= 1:
        for (x, y, w, h) in detectado:
            cv2.rectangle(copia, (x, y), (x + w, y + h), (500, 600, 10), 3)
        pathSalida = pathSalida + str(contador)+".jpg"
        print(pathSalida)
        cv2.imwrite(pathSalida, copia)

    del clasificador


substractorKNN = cv2.createBackgroundSubtractorKNN(
    history=500,
    dist2Threshold=400,
    detectShadows=False
)
cv2.ocl.setUseOpenCL(False)

captura = cv2.VideoCapture(0)
hilos = list()
i = 0

while True:
    a, capturado = captura.read()

    if not a:
        break

    if cv2.waitKey(30) & 0xff == ord("s"):
        break

    contornosimg = substractorKNN.apply(capturado).copy()
    contornos, _ = cv2.findContours(
        contornosimg,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for c in contornos:
        if cv2.contourArea(c) > 100000:
            print("Hay movimiento!!")
            t = hilo.Thread(target=guardarImagenObjeto(capturado, i))
            hilos.append(t)
            t.start()
            i+=1

    cv2.imshow('Captura', capturado)

captura.release()
cv2.destroyAllWindows()

