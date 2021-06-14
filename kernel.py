import cv2
import numpy as np

img = cv2.imread("./loro.jpg")

kernel = np.float32([[2, 4, 5, 4, 2], [4, 9, 12, 9, 4], [5, 12, 15, 12, 5], [4, 9, 12, 9, 4], [2, 4, 5, 4, 2]]) / 159


blur = cv2.filter2D(img, -1, kernel)

cv2.imshow('original', img)
cv2.imshow('kernel', blur)


cv2.imwrite('canny.png', blur)


cv2.waitKey(5)
