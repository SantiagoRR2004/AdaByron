# https://aceptaelreto.com/problem/statement.php?id=762

"""
Esto es un problema de geometría
Tenemos un rectángulo que queremos que pase
por una esquina. Sabemos el ancho de los pasillos
que conectan a la esquina.
Como el rectángulo se empuja siempre por su 
lado más corto tiene que girar cuando da el giro de 90 grados.
"""

import sys
import math

for line in sys.stdin:
    anchoPiano, largoPiano, anchoPasillo1, anchoPasillo2 = [
        int(x) for x in line.strip().split()
    ]

    ladoCorto = min(anchoPiano, largoPiano)
    ladoLargo = max(anchoPiano, largoPiano)
    radiant90 = math.pi / 2

    """
    Las coordenadas 0,0 es el punto de la esquina exterior
    Lo que vamos a hacer es pegar el piano a la pared exterior
    e ir rotándolo lentamente. Sabemos que no cabe si las dos
    esquinas del piano que no están pegadas a la pared exterior
    hacen una recta que pasa por fuera de la esquina interior de la curva.
    """

    for i in range(ladoLargo + 1):
        angle1 = math.acos(i / ladoLargo)
        x1 = i + math.cos(radiant90 - angle1) * ladoCorto
        y1 = math.sin(radiant90 - angle1) * ladoCorto
        j = (ladoLargo**2 - i**2) ** (1 / 2)
        x2 = math.sin(angle1) * ladoCorto
        y2 = j + math.cos(angle1) * ladoCorto

        # Orientation of 3 ordered points
        # It can't be counterclockwise

        if (x2 - x1) * (anchoPasillo2 - y1) - (anchoPasillo1 - x1) * (y2 - y1) > 0:
            print("NO")
            break
    else:
        print("SI")
