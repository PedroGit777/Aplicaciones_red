import socket
import os
import numpy as np
from datetime import date

PORT = 65432
buffer_size = 1024
print('introduce tu fecha de nacimiento')
Dia=int(input('dia(DD):'))
Mes=int(input('Mes(MM):'))
Año: int=int(input('Añ0(AAAA):'))
d0 = date(2021,8,26)
d1 = date(Año,Mes,Dia)
delta = d0 - d1
print(delta.days%3)
HOST = str(input('ingresa la IP del servidor'))


def menu():
    os.system('cls')
    print('Selecciona la dificultad ')
    print('1- Principiante(9x9)')
    print('2- Avanzado(16x16)')
    print('3- Salir')


def construir_tablero(n):
    m = np.zeros((n, n))
    # identificar columnas y filas
    for i in range(len(m) - 1):
        m[0][i + 1] = i + 1
    for i in range(len(m) - 1):
        m[i + 1][0] = i + 1
    return m


def tirarx():
    x = input("inserta el numero de columna >> ")
    return x


def tirary():
    y = input("inserta el numero de fila >> ")
    return y


def dibujatablero(M):
    print(M)


def minar():
    m = socket_cliente.recv(buffer_size).decode()
    print(m)


def principiante():
    print('dificultad principiante\n')
    n = 10

    t = construir_tablero(n)
    dibujatablero(t)

    for i in [0, 1, n]:
        x = tirarx()
        equis = bytes(x, encoding='ascii')
        socket_cliente.sendall(equis)
        y = tirary()
        ye = bytes(y, encoding='ascii')
        socket_cliente.sendall(ye)
        flag = socket_cliente.recv(buffer_size)
        flag = flag.decode('ascii')
        if flag == "1":
            print('perdiste')
            minar()
            return 0
        elif flag == "0":
            t[int(y)][int(x)] = 1
            print(t)


def avanzado():
    print('dificultad de avanzado \n\n')
    n = 17

    t = construir_tablero(n)
    dibujatablero(t)
    for i in [0, 1, n]:
        x = tirarx()
        equis = bytes(x, encoding='ascii')
        socket_cliente.sendall(equis)
        y = tirary()
        ye = bytes(y, encoding='ascii')
        socket_cliente.sendall(ye)
        flag = socket_cliente.recv(buffer_size)
        flag = flag.decode('ascii')
        if flag == "1":
            print("perdiste")
            minar()
            return 0
        elif flag == "0":
            t[int(y)][int(x)] = 1
            print(t)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_cliente:
    socket_cliente.connect((HOST, PORT))

    while True:
        # Mostramos el menu
        menu()

        # solicituamos una opción al usuario
        opcionMenu = input("opcion >> ")
        aux = bytes(opcionMenu, encoding='ascii')
        socket_cliente.sendall(aux)
        if (opcionMenu == '1'):
            principiante()
        elif (opcionMenu == '2'):

            avanzado()
        elif (opcionMenu == '3'):

            break

        else:

            input('opcion no valida')

