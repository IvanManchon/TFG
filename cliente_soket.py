import socket

while 1:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.0.17', 10000)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:
        # Send data
        message = b'Pack_envio'
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 1
        amount_expected = len(message)

        if amount_received > 0:
            data = sock.recv(1000)
            amount_received += len(data)
            print('received {!r}'.format(data))

    finally:
        print('closing socket')
        sock.close()
    matriz = data.decode("utf-8")
    print(matriz)
    print('----------------------------------')
    print()
