import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
import keyboard
from pyzbar.pyzbar import decode

captura = cv2.VideoCapture(0)
captura.set(3, 640)
captura.set(4, 480)


def nothing(x):
    pass


def crear_barras():
    cv2.namedWindow('Ajuste')
    cv2.resizeWindow('Ajuste', 400, 200)
    # cv2.createTrackbar('Size(%)', 'Ajuste', 20, 100, nothing)
    cv2.createTrackbar('Umbral', 'Ajuste', 0, 254, nothing)
    cv2.createTrackbar('Blur', 'Ajuste', 1, 21, nothing)


crear_barras()


def valor_barra():
    # Tamano = cv2.getTrackbarPos('Size(%)', 'Ajuste')
    Umbral = cv2.getTrackbarPos('Umbral', 'Ajuste')
    medianblur = cv2.getTrackbarPos('Blur', 'Ajuste')
    return Umbral, medianblur


def BlancoYNegro(Mat, Umbral):
    RX = np.size(Mat, 0)
    RY = np.size(Mat, 1)
    for i in range(RX):
        for j in range(RY):
            if Mat[i, j] >= Umbral:
                Mat[i, j] = 255
            else:
                Mat[i, j] = 0
    return Mat


def Ajustar_imagen():
    L = [0, 0]
    while True:
        # ret, img = captura.read()
        # cv2.imwrite('foto.png', img)
        original = cv2.imread("./pelota.jpg")
        small = cv2.resize(original, (400, 300))

        gris_m = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('Gris.png', gris_m)
        gris = cv2.imread("./Gris.png")

        Umbral = valor_barra()[0]
        L[0] = Umbral
        gris2 = BlancoYNegro(gris_m, L[0])
        # gris2 = cv2.threshold(gris_m, Umbral, 255, cv2.THRESH_BINARY)

        mb = valor_barra()[1]
        L[1] = mb
        blur = cv2.medianBlur(gris2, mb)

        cv2.imwrite('Gris_umbral.png', blur)
        gris_u_b = cv2.imread("./Gris_umbral.png")
        cv2.imshow('Resumen', cv2.vconcat([small, gris, gris_u_b]))

        if keyboard.is_pressed('f'):
            break
        cv2.waitKey(1)
    cv2.destroyAllWindows()
    return L[0], L[1]


U, B = Ajustar_imagen()
print(U, B)


def Camara(U, B):
    # ret, img = captura.read()
    img = cv2.imread("./1.png")
    gris_m = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # gris2 = BlancoYNegro(gris_m, U)
    blur = cv2.medianBlur(gris_m, B)
    code = decode(blur)
    if code:
        for i in range(len(code)):
            print(code[i].data)
            rect = np.array(code[i].polygon)
            print(rect)
            cv2.polylines(img, [rect], True, (0, 0, 255), 2)
        cv2.imshow('Detection', img)
    cv2.waitKey(1)
    Camara(U, B)


Camara(U, B)
captura.release()
