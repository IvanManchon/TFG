import cv2
import time
import numpy as np
from pyzbar.pyzbar import decode
import socket

# captura = cv2.VideoCapture(0)
# captura.set(3, 640)
# captura.set(4, 480)
lista_centros_copia = []

# Crear TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Servidor
server_address = (socket.gethostbyname(socket.gethostname()), 10000)
print('Iniciando servidor en {} puerto {}'.format(*server_address))
sock.bind(server_address)

# Escucha
sock.listen(1)

def conexion(pack_envio):
    # Espera
    print('Esperando peticiones...')
    connection, client_address = sock.accept()
    try:
        print('Conexión con ', client_address)
        # Informacion
        data = connection.recv(1024)
        print('Petición de {!r}'.format(data))
        if data:
            print('Enviando información')
            connection.send(bytes(str(pack_envio), encoding = "utf-8"))
            print('*******************************************')
            print(pack_envio)
            print('*******************************************')
    finally:
        # Limpiar conexion
        # connection.close()
        pass

def ordena(lista):
    ordena = len(lista)*[0]
    for i in range(len(lista)):
        p = lista[i]
        p2 = p[0]-1
        ordena[p2] = lista[i]
    return ordena

def centro(dato, puntos):
    lx = []
    ly = []
    for j in range(len(puntos)):
        lx.append(puntos[j][0])
        ly.append(puntos[j][1])
    minX = min(lx)
    minY = min(ly)
    maxX = max(lx)
    maxY = max(ly)

    cx = minX + int((maxX - minX) / 2)
    cy = minY + int((maxY - minY) / 2)
    lista = cx, cy

    return int(dato), lista

def velocidades(lista1, lista2):
    lx1 = []
    ly1 = []
    lx2 = []
    ly2 = []
    lx = []
    ly = []
    vel = []
    for j in range(len(lista1)):
        lx1.append(lista1[j][1][0])
        ly1.append(lista1[j][1][1])
        lx2.append(lista2[j][1][0])
        ly2.append(lista2[j][1][1])
        lx.append(lx2[0]-lx1[0])
        ly.append(ly2[0]-ly1[0])
    for z in range(len(lx)):
        l = (lista1[z][0], (lx[z], ly[z]))
        vel.append(l)
    return vel

while 1:
    pack_envio = []
    lista_centros = []
    t1 = time.time()
    # ret, img = captura.read()
    img = cv2.imread("./ORDENAR.jpg")

    # BGR to RGB
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # KERNEL
    kernel = np.float32([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
    # kernel = np.float32([[1, 1, 1], [1, 1, 1], [1, 1, 1]]) / 9
    # kernel = np.float32([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6],
    #                     [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]]) / 256

    # PROCESO
    blur = cv2.filter2D(rgb, -1, kernel)
    code = decode(blur)
    pack_envio.append(len(code))
    if code:
        puntos_lista = []
        datos = []
        for i in range(len(code)):
            dato = code[i].data
            d = dato.decode("utf-8")
            datos.append(d)
            rect = np.array(code[i].polygon)
            cv2.polylines(img, [rect], True, (0, 0, 255), 2)
            agentes, punto = centro(d, rect)
            puntos_lista.append(centro(d, rect))
            lista_centros.append(punto)
        lista_centros = (ordena(puntos_lista))
        if len(lista_centros_copia) == 0:
            lista_centros_copia = lista_centros
        # cv2.imshow('Detection', img)
        pack_envio.append(lista_centros)
    cv2.waitKey(1)

    pack_envio.append(velocidades(lista_centros, lista_centros_copia))
    lista_centros_copia = lista_centros

    t3 = time.time()
    conexion(pack_envio)
    t4 = time.time()

    # VISUALIZAR/ENVIO DATOS
    print('Tamaño de imagen:', blur.shape[:2])
    print('Numero de Agentes:', pack_envio[0])
    print('Posiciones:', pack_envio[1])
    print('Velocidades:', pack_envio[2])
    t2 = time.time()
    print('Tiempo de envio:', t4 - t3)
    print('Tiempo Total:', t2 - t1)
    print('-------------------------------------------')
