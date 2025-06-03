# https://aceptaelreto.com/problem/statement.php?id=749


cols, rows, gaps = [int(x) for x in input().split()]


while cols != 0 and rows != 0:

    # Horizontal and vertical connections with padding
    # Padding is to avoid index errors when checking adjacent cells
    # and eliminate ifs
    horizontal = (
        [[0] * (cols + 2)]
        + [[0] + [1 for x in range(cols - 1)] + [0] for y in range(rows)]
        + [[0] * (cols + 2)]
    )
    vertical = (
        [[0] * (cols + 2)]
        + [[0] + [1 for x in range(cols)] + [0] for y in range(rows - 1)]
        + [[0] * (cols + 2)]
    )

    if gaps > 0:

        intersections = [int(x) for x in input().split()]
        intersections = [
            intersections[i : i + 2] for i in range(0, len(intersections), 2)
        ]

        for col, row in intersections:
            # Eliminate connection to the left
            horizontal[row][col - 1] = 0
            # Eliminate connection to the right
            horizontal[row][col] = 0
            # Eliminate connection upwards
            vertical[row - 1][col] = 0
            # Eliminate connection downwards
            vertical[row][col] = 0

    # The connections left are the number of buildings
    print(sum([sum(x) for x in horizontal]) + sum([sum(x) for x in vertical]))

    cols, rows, gaps = [int(x) for x in input().split()]

"""
Pista 1
Calcula el número de edificios totales asumiendo que no hay ninguna intersección que falte, 
y luego ve restando edificios en función de las intersecciones no construídas.

Pista 2
Cada intersección ausente hace imposible la construcción de 2, 3 o 4
edificios dependiendo de si está en una esquina, un lateral, o la zona central.

Pista 3
Si hay dos intersecciones ausentes adyacentes, ambas afectan al mismo edificio, 
que debe contarse únicamente una vez.

Pista 4
Si hay dos intersecciones adyacentes ausentes, decide cuál será la responsable de 
contar como no construído el edificio que comparten.

Pista 5
Al recorrer las intersecciones no construídas, mira si en la lista de intersecciones 
están las adyacentes responsables de contar los edificios para no contarlos dos veces.

Pista 6
Averigua de forma eficiente si en la lista de intersecciones están las adyacentes o tardarás demasiado tiempo.
"""
