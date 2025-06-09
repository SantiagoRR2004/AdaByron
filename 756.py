# https://aceptaelreto.com/problem/statement.php?id=756

import sys

for line in sys.stdin:
    inversiones = 0

    piezas = [int(num) for num in line.split()]

    for i in range(len(piezas)):
        for j in range(i + 1, len(piezas)):
            if piezas[i] > piezas[j]:
                inversiones += 1

    if inversiones % 2 == 0:
        print("SI")
    else:
        print("NO")
