import qrcode

codigo = input("Codigo QR: ")
imagen = qrcode.make(codigo)
imagen.save(open(codigo + '.png','wb'))
