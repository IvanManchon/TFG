import cv2
import numpy as np
import time

cam = cv2.VideoCapture(0)
# LISTA VELOCIDAD
Vx = []
Vy = []

while 1:
    t1 = time.time()
    # FOTO
    # _, img = cam.read()
    img = cv2.imread("./PAINTNEGRO.jpg")

    # KERNEL
    # kernel = np.float32([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9
    kernel = np.float32([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
    # kernel = np.float32([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6],
    #                     [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]]) / 256
    img_kernel = cv2.filter2D(img, -1, kernel)

    # BGR to HSV
    hsv = cv2.cvtColor(img_kernel, cv2.COLOR_BGR2HSV)

    # BLUE HSV
    lower_blue = np.array([90, 120, 120])
    upper_blue = np.array([130, 255, 255])

    # GREEN HSV
    lower_green = np.array([50, 120, 120])
    upper_green = np.array([100, 255, 255])

    # RED HSV
    lower_red1 = np.array([0, 120, 120])
    upper_red1 = np.array([20, 255, 255])

    lower_red2 = np.array([170, 120, 120])
    upper_red2 = np.array([180, 255, 255])

    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.add(mask_red1, mask_red2)

    # MASCARA
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue_green = cv2.add(mask_blue, mask_green)
    mask = cv2.add(mask_blue_green, mask_red)
    res = cv2.bitwise_and(img, img, mask=mask)

    # CONTORNOS
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # LISTAS POSICIÓN
    Lx = []
    Ly = []

    for i in contours:
        area = cv2.contourArea(i)
        if area >= 1000:
            pixel = cv2.moments(i)
            if pixel["m00"] == 0:
                pixel["m00"] = 1
            px = int(pixel['m10'] / pixel['m00'])
            py = int(pixel['m01'] / pixel['m00'])
            cv2.drawContours(res, [i], -1, (255, 255, 255), 2)
            cv2.circle(res, (px, py), 4, (0, 0, 0), -1)
            Lx.append(px)
            Ly.append(py)

    # IMPRIMIR
    cv2.imshow('frame', img)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    t2 = time.time()
    print('Tiempo:', t2-t1)
    print('Posición:', Lx, Ly)

cv2.destroyAllWindows()
