# https://aceptaelreto.com/problem/statement.php?id=749


cols, rows, gaps = [int(x) for x in input().split()]


while cols != 0 and rows != 0:

    horizontalTotal = (cols - 1) * rows
    verticalTotal = (rows - 1) * cols

    horizontalSet = set()
    verticalSet = set()

    if gaps > 0:
        intersections = [int(x) for x in input().split()]
        intersections = [
            intersections[i : i + 2] for i in range(0, len(intersections), 2)
        ]

        for x, y in intersections:
            # Add top
            verticalSet.add((x, max(y - 1, 1)))
            # Add bottom
            verticalSet.add((x, min(y, rows - 1)))
            # Add left
            horizontalSet.add((max(x - 1, 1), y))
            # Add right
            horizontalSet.add((min(x, cols - 1), y))

    print(horizontalTotal + verticalTotal - len(horizontalSet) - len(verticalSet))

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
