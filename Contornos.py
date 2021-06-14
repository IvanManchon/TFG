import cv2
import time
import matplotlib.pyplot as plt
import numpy as np

t1 = time.time()
# TRANSFORMAMOS LA IMAGEN A BLANCO Y NEGRO
def BlancoYNegro(Mat,Umbral,intensidad):
    Mat2 = Mat
    for i in range(np.size(Mat, 0) - 1):
        for j in range(np.size(Mat, 1) - 1):
            if Mat[i, j] <= Umbral:
                Mat2[i, j] = intensidad
            else:
                Mat2[i, j] = 0
    return(Mat)

# COMPRUEBA A SUS 8 VECINOS
def Vecinos8(Mat,intensidad):
    pixels = []
    for i in range(np.size(Mat, 0) - 1):
        for j in range(np.size(Mat, 1) - 1):
            if Mat[i,j] == intensidad:
                if Mat[i-1,j-1] == intensidad:
                    pixel = [i - 1, j - 1]
                    pixels.append(pixel)

                elif Mat[i,j-1] == intensidad:
                    pixel = [i, j - 1]
                    pixels.append(pixel)

                elif Mat[i+1,j-1] == intensidad:
                    pixel = [i + 1, j - 1]
                    pixels.append(pixel)

                elif Mat[i-1,j] == intensidad:
                    pixel = [i - 1, j]
                    pixels.append(pixel)

                elif Mat[i,j] == intensidad:
                    pixel = [i, j]
                    pixels.append(pixel)

                elif Mat[i+1,j] == intensidad:
                    pixel = [i +1, j]
                    pixels.append(pixel)

                elif Mat[i-1,j+1] == intensidad:
                    pixel = [i - 1, j + 1]
                    pixels.append(pixel)

                elif Mat[i,j+1] == intensidad:
                    pixel = [i, j + 1]
                    pixels.append(pixel)

                elif Mat[i+1,j+1] == intensidad:
                    pixel = [i + 1, j + 1]
                    pixels.append(pixel)
    print('MODELO VECINOS 8')
    return pixels

# COMPRUEBA A SUS 4 VECINOS
def Vecinos4(Mat,intensidad):
    pixels = []
    for i in range(np.size(Mat, 0) - 1):
        for j in range(np.size(Mat, 1) - 1):
            if Mat[i,j] == intensidad:
                if Mat[i,j-1] == intensidad:
                    pixel = [i, j - 1]
                    pixels.append(pixel)

                elif Mat[i+1,j] == intensidad:
                    pixel = [i + 1, j]
                    pixels.append(pixel)

                elif Mat[i-1,j] == intensidad:
                    pixel = [i - 1, j]
                    pixels.append(pixel)

                elif Mat[i,j] == intensidad:
                    pixel = [i, j]
                    pixels.append(pixel)

                elif Mat[i,j+1] == intensidad:
                    pixel = [i, j + 1]
                    pixels.append(pixel)
    print('MODELO VECINOS 4')
    return pixels

# OBTENEMOS EL CENTRO DE LA FIGURA
def centro(lista):
    lista_x = []
    lista_y = []
    for z in lista:
        if z[1] not in lista_x:
            lista_x.append(z[1])
        elif z[0] not in lista_y:
            lista_y.append(z[0])
    minX = min(lista_x)
    maxX = max(lista_x)
    minY = min(lista_y)
    maxY = max(lista_y)

    centroX = (maxX - minX) / 2 + minX
    centroY = (maxY - minY) / 2 + minY
    return centroX,centroY

# LEEMOS LA IMAGEN
imagen_real = cv2.imread("./FLECHA.jpg")

# SIMPLIFICAMOS LA IMAGEN PARA TENER MENOS PIXELES CON LOS QUE TRABAJAR
# PERDEREMOS PRECISIÓN, PERO GANAREMOS RENDIMIENTO
reduccion = 0.2;
imagen = cv2.resize(imagen_real, (0,0), fx = reduccion, fy = reduccion)

# ELIMINAMOS LOS COLORES Y LO DEJAMOS EN ESCALA DE GRISES
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# AJUSTAMOS EL UMBRAL Y LA INTENSIDAD PARA REPRESENTAR LA IMAGEN
umbral = 200
intensidad = 255
gris2 = BlancoYNegro(gris,umbral,intensidad)

# SELECCIONAMOS EL TIPO DE COMPROBACIONES QUE REALIZAMOS
pixels = Vecinos8(gris2,intensidad)
#pixels = Vecinos4(gris2,intensidad)

# GUARDAMOS EL CENTRO DE LA FIGURA
puntoX,puntoY = centro(pixels)


# REPRESENTAMSO LAS DISTINTAS IMAGENES SEGÚN SE NECESITE
# cv2.imshow('IMAGEN PRUEBA', imagen)
# cv2.imshow('IMAGEN PRUEBA GRIS', gris)
# cv2.imshow('IMAGEN PRUEBA GRIS2', gris2)

# REAJUSTAMOS LA IMAGEN A LA ORIGINAL Y PLOTEAMOS JUNTO AL CENTRO
aumento = 1/reduccion
cv2.circle(imagen_real,(round(aumento*puntoX),round(aumento*puntoY)),3,(0,0,255),10)
cv2.imshow('IMAGEN PRUEBA PUNTO', imagen_real)
cv2.imwrite('IMAGEN_PRUEBA_PUNTO_FLECHA.png',imagen_real)

print('EJE X:', round(aumento*puntoX))
print('EJE Y:', round(aumento*puntoY))

t2 = time.time()

print('Tiempo:', t2-t1)

cv2.waitKey(0)
cv2.destroyAllWindows()