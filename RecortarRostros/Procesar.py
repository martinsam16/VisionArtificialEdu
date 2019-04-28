import cv2
import numpy as np
import glob

pathCascada = "Cascadas/haarcascade_frontalface_alt.xml"
clasificadorRostro = cv2.CascadeClassifier(pathCascada)

nroFoto = 0
pathSalida = "Salida/"

for imagenLeida in glob.glob("Entrada/*.JPG"):

    imagen = cv2.imread(imagenLeida)
    rostros = clasificadorRostro.detectMultiScale(
        imagen,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(20, 20)
    )

    for (x, y, w, h) in rostros:
        cortar = np.array(imagen[y:y + h, x:x + w])
        cv2.imwrite(pathSalida + str(nroFoto) + '.jpg', cortar)
        nroFoto += 1
        print("Rostros Procesadas ---> "+str(nroFoto))

print("Finalizado")


