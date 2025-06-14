# https://aceptaelreto.com/problem/statement.php?id=762
# https://www.reddit.com/r/MathHelp/comments/15eieh7/optimizing_the_ladder_around_a_corner/
# https://www.youtube.com/watch?v=Z32-3iVXdwc

"""
Esto es un problema de geometría
Tenemos un rectángulo que queremos que pase
por una esquina. Sabemos el ancho de los pasillos
que conectan a la esquina.
Como el rectángulo se empuja siempre por su
lado más corto tiene que girar cuando da el giro de 90 grados.
"""

import sys


def polinomioEsquina(
    hallWidthA: float, hallWidthB: float, objectWidth: float, slope: float
) -> float:
    """
    Calcula el valor del polinomio que representa
    la condición de que un objeto rectangular
    pueda girar en una esquina de 90 grados
    entre dos pasillos de anchos dados.
    """
    aSquared = hallWidthA * hallWidthA
    bSquared = hallWidthB * hallWidthB
    wSquared = objectWidth * objectWidth
    mSquared = slope * slope
    mCubed = mSquared * slope
    mFourth = mCubed * slope
    mSixth = mFourth * mSquared
    return (
        (bSquared - wSquared) * mSixth
        + wSquared * mFourth
        - 2 * hallWidthA * hallWidthB * mCubed
        + wSquared * mSquared
        + (aSquared - wSquared)
    )


def ajustarPendiente(comienzo: float, fin: float, anchoObjeto: float) -> float:
    """
    Encuentra la pendiente más ajustada para que un objeto rectangular
    pueda girar en una esquina de 90 grados entre dos pasillos
    """
    # https://en.wikipedia.org/wiki/Bisection_method
    if comienzo == fin:
        return 1

    lowerLimit = 0
    upperLimit = pow(comienzo / fin, 1 / 3)
    pendiente = 0

    for _ in range(100):  # Suficientes iteraciones para precisión
        pendiente = (lowerLimit + upperLimit) / 2

        # Find the value of the polynomial at this point
        evaluacion = polinomioEsquina(comienzo, fin, anchoObjeto, pendiente)

        if evaluacion < 0:
            # If the polynomial is negative, we need a larger pendiente
            upperLimit = pendiente
        else:
            # If the polynomial is positive, we need a smaller pendiente
            lowerLimit = pendiente

    return pendiente


def longitud_max(
    ancho1: float, ancho2: float, anchObjeto: float, pendiente: float
) -> float:
    """
    Calcula la longitud máxima de un objeto rectangular que puede girar
    en una esquina de 90 grados entre dos pasillos de anchos dados.
    """
    angleFactor = 1 + 1 / (pendiente * pendiente)
    distanciaEfectiva = (
        pendiente * ancho2
        + ancho1
        - anchObjeto * pow(pendiente ** 2 + 1, 0.5)
    )
    distanciaEfectiva = distanciaEfectiva ** 2
    return pow(angleFactor * distanciaEfectiva, 0.5)


for line in sys.stdin:
    anchoPiano, largoPiano, anchoPasillo1, anchoPasillo2 = [
        int(x) for x in line.strip().split()
    ]

    ladoCorto = min(anchoPiano, largoPiano)
    ladoLargo = max(anchoPiano, largoPiano)

    if ladoCorto > anchoPasillo1 or ladoCorto > anchoPasillo2:
        print("NO")
        continue

    # Aseguramos que anchoPasillo1 es el más pequeño
    if anchoPasillo1 > anchoPasillo2:
        anchoPasillo1, anchoPasillo2 = anchoPasillo2, anchoPasillo1

    slope = ajustarPendiente(anchoPasillo1, anchoPasillo2, ladoCorto)
    longitudMax = longitud_max(anchoPasillo1, anchoPasillo2, ladoCorto, slope)
    if ladoLargo <= longitudMax:
        print("SI")
    else:
        print("NO")
