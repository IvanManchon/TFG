import cv2
import time
import numpy as np

# cam = cv2.VideoCapture(0)

while True:
    t1 = time.time()
    # FOTO
    # _, img = cam.read()
    img = cv2.imread("./PAINTNEGRO.jpg")

    # BGR to RGB
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # KERNEL
    # kernel = np.float32([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
    kernel = np.float32([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9
    # kernel = np.float32([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6],
    #                     [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]]) / 256

    # ENFOCAR
    # kernel = np.float32([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    # CONTRASTE
    # cv.equalizeHist(img)

    # FONDO
    shape = np.zeros(img.shape[:2], np.uint8)

    # UMBRALES
    umbralb = 70
    umbralr = 30
    umbralg = 170

    # VARIABLES
    cannyalto = 75
    cannybajo = 20

    areamin = 0
    Lx = []
    Ly = []

    # BLUE RGB
    blue = rgb[:, :, 2]
    bluef = cv2.filter2D(blue, -1, kernel)
    # bluee = cv2.equalizeHist(bluef)
    hist, bins = np.histogram(bluef.flatten(), 256, [0, 256])
    bluec = cv2.Canny(bluef, cannybajo, cannyalto)
    cb, _ = cv2.findContours(bluec, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in cb:
        area = cv2.contourArea(i)
        cv2.drawContours(bluec, [i], -1, (255, 0, 0), 2)
        pixel = cv2.moments(i)
        if pixel["m00"] == 0:
            pixel["m00"] = 1
        px = int(pixel['m10'] / pixel['m00'])
        py = int(pixel['m01'] / pixel['m00'])
        Lx.append(px)
        Ly.append(py)
        if bluef[px, py] <= umbralb:
            cv2.circle(bluec, (px, py), 4, (255, 0, 0), -1)

    # GREEN RGB
    green = rgb[:, :, 1]
    greenf = cv2.filter2D(green, -1, kernel)
    # greene = cv2.equalizeHist(greenf)
    hist, bins = np.histogram(greenf.flatten(), 256, [0, 256])
    greenc = cv2.Canny(greenf, cannybajo, cannyalto)
    cg, _ = cv2.findContours(greenc, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in cg:
        area = cv2.contourArea(i)
        if area > areamin:
            cv2.drawContours(greenc, [i], -1, (255, 255, 255), 2)
            pixel = cv2.moments(i)
            if pixel["m00"] == 0:
                pixel["m00"] = 1
            px = int(pixel['m10'] / pixel['m00'])
            py = int(pixel['m01'] / pixel['m00'])
            if greenf[px, py] >= umbralg:
                cv2.circle(greenc, (px, py), 4, (255, 255, 255), -1)

    # RED RGB
    red = rgb[:, :, 0]
    redf = cv2.filter2D(red, -1, kernel)
    # rede = cv2.equalizeHist(redf)
    hist, bins = np.histogram(redf.flatten(), 256, [0, 256])
    redc = cv2.Canny(redf, cannybajo, cannyalto)
    cr, _ = cv2.findContours(redc, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in cr:
        area = cv2.contourArea(i)
        if area > areamin:
            cv2.drawContours(redc, [i], -1, (255, 255, 255), 2)
            pixel = cv2.moments(i)
            if pixel["m00"] == 0:
                pixel["m00"] = 1
            px = int(pixel['m10'] / pixel['m00'])
            py = int(pixel['m01'] / pixel['m00'])
            if redf[px, py] >= umbralr:
                cv2.circle(redc, (px, py), 4, (255, 255, 255), -1)

    # IMPRIMIR
    cv2.imshow('original', img)
    cv2.imshow('blue', bluec)
    cv2.imshow('red', redc)
    cv2.imshow('green', greenc)

    cv2.imshow('blue rgb', blue)
    cv2.imshow('red rgb', red)
    cv2.imshow('green rgb', green)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    t2 = time.time()
    print(t2-t1)

cv2.destroyAllWindows()