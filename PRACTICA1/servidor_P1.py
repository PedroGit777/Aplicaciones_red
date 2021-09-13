import socket
import numpy as np
import time
HOST = "localhost"
PORT = 65432
buffer_size = 1024


def minas(n):
    if n == 10:
        print("Se colocaron 10 minas")
        x = np.random.randint(1, 9, (10, 2))
        print(f'x= {x}')
        return x
    elif n == 17:
        print("Se colocaron 40 minas")
        x = np.random.randint(1, 16, (40, 2))
        return x

def minar (cormin,m):
    for i in range(len(cormin)):
        x = cormin[i][1]
        y = cormin[i][0]
        m[int(y)][int(x)] = 2
    m = str(m)

    cliente_conexion.sendall(m.encode())





def principiante():
    n = 10
    m = np.zeros((n, n))
    print(m)
    for i in range(len(m)-1):
        m[0][i+1]=i+1
    for i in range(len(m)-1):
        m[i+1][0] = i + 1
    cormin = minas(n)
    print(f'cormin: {cormin}')
    tiros = np.zeros((n, 2))
    for i in range(len(tiros)):
        x = cliente_conexion.recv(buffer_size).decode()

        tiros[i][1] = x
        y = cliente_conexion.recv(buffer_size).decode()
        tiros[i][0] = y
        print("El tiro fue x:", tiros[i][1], " y:",tiros[i][0])
        aux = 0
        for j in range(len(cormin)):
            if (int(cormin[j][0]) == int(tiros[i][0])) and (int(cormin[j][1]) == int(tiros[i][1])):
                aux = 1
                break
        if aux == 1:
            flag = "1"
            cliente_conexion.sendall(flag.encode())
            minar(cormin,m)
            return 0
        elif aux == 0:
            flag = "0"
            m[int(y)][int(x)] = 1
            cliente_conexion.sendall(flag.encode())

        # elif aux == 0:
def avanzado():
    n = 17
    m = np.zeros((n, n))
    for i in range(len(m) - 1):
        m[0][i + 1] = i + 1
    for i in range(len(m) - 1):
        m[i + 1][0] = i + 1
    cormin = minas(n)
    print(cormin)
    tiros = np.zeros((n, 2))

    for i in range(len(tiros)):
        x = cliente_conexion.recv(buffer_size)
        x = x.decode('ascii')
        tiros[i][1] = x
        y = cliente_conexion.recv(buffer_size)
        y = y.decode('ascii')
        tiros[i][0] = y
        print("El tiro fue x:", tiros[i][1], " y:",tiros[i][0])
        aux = 0
        for j in range(len(cormin)):
            if (int(cormin[j][0]) == int(tiros[i][0])) and (int(cormin[j][1]) == int(tiros[i][1])):
                aux = 1
                break
        if aux == 1:
            print("perdiste")
            flag = "1"
            cliente_conexion.sendall(flag.encode())
            minar(cormin, m)
            return 0
        elif aux == 0:
            flag = "0"
            m[int(y)][int(x)] = 1
            cliente_conexion.sendall(flag.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_servidor:
    socket_servidor.bind((HOST, PORT))
    socket_servidor.listen()
    cliente_conexion, addr = socket_servidor.accept()
    with cliente_conexion:
        print(f'Conectado con, {addr}')
        while True:
            data = cliente_conexion.recv(buffer_size).decode()

            print("Recibido opcion ", data, "   de ", addr)
            if data == "1":

                principiante()

            elif data == "2":

                avanzado()
            elif data == "3":
                break
            if not data:
                break

            cliente_conexion.sendall(b"bye")