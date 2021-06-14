import socket
import sys
# Crear TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Servidor
server_address = (socket.gethostbyname(socket.gethostname()), 10000)
print('Iniciando servidor en {} puerto {}'.format(*server_address))
sock.bind(server_address)

# Escucha
sock.listen(1)

n = -2

while True:
    n += 1
    envio = str(n)
    # Espera
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Informacion
        while True:
            data = connection.recv(1000)
            if data:
                print('received {!r}'.format(data))
                print('sending data back to the client')
                connection.send(str(envio).encode())
                print(str(envio).encode(encoding = "utf-8"))
                print(envio)
            else:
                break
    finally:
        # Limpiar conexion
        connection.close()