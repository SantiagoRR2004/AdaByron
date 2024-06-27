#  https://aceptaelreto.com/problem/statement.php?id=744

import sys


def calcular_min_mensajes(tiempo_max, felicitaciones):
    # Inicializar contador de mensajes
    mensajes = 0
    i = 0
    n = len(felicitaciones)

    while i < n:
        # Incrementamos el contador de mensajes
        mensajes += 1
        # Determinamos el límite máximo para el siguiente agradecimiento
        limite = felicitaciones[i] + tiempo_max

        # Avanzamos el índice hasta que la felicitación salga del límite permitido
        while i < n and felicitaciones[i] <= limite:
            i += 1

    return mensajes


input = sys.stdin.read

data = input().strip().split("\n")
index = 0

while index < len(data):
    time = int(data[index])
    index += 1
    list1 = [int(x) for x in data[index].split()][:-1]
    index += 1
    maxTime = calcular_min_mensajes(time, list1)
    print(maxTime)
