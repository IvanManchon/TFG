import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
import keyboard
from pyzbar.pyzbar import decode

captura = cv2.VideoCapture(0)
captura.set(3, 640)
captura.set(4, 480)


def Camara():
    while True:
        t1 = time.time()
        # ret, img = captura.read()
        img = cv2.imread("./COPIA.png")

        # BGR to RGB
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # kernel
        # kernel = np.float32([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
        kernel = np.float32([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9

        # kernel = np.float32([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6],
        #                     [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]]) / 256

        # ENFOCAR
        # kernel = np.float32([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

        blur = cv2.filter2D(rgb, -1, kernel)
        code = decode(blur)
        if code:
            c = []
            for i in range(len(code)):
                print(code[i].data)
                rect = np.array(code[i].polygon)
                #print(rect)
                cv2.polylines(img, [rect], True, (0, 0, 255), 2)
            for j in range(4):
                c.append(list(rect[j]))
            cv2.imshow('Detection', img)
            cv2.imwrite('QR_identificado.png', img)
            print(c)
        cv2.waitKey(1)
        t2 = time.time()
        print(t2 - t1)

Camara()
