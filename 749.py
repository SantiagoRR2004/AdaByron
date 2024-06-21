# https://aceptaelreto.com/problem/statement.php?id=749


cols, rows, gaps = [int(x) for x in input().split()]


while cols != 0 and rows != 0:

    horizontal = [[1 for x in range(cols - 1)] for y in range(rows)]
    vertical = [[1 for x in range(cols)] for y in range(rows - 1)]

    if gaps > 0:

        intersections = [int(x) for x in input().split()]
        intersections = [
            intersections[i : i + 2] for i in range(0, len(intersections), 2)
        ]

        for col, row in intersections:
            if col > 1:
                # Eliminate connection to the left
                horizontal[row - 1][col - 2] = 0
            if col < cols:
                # Eliminate connection to the right
                horizontal[row - 1][col - 1] = 0
            if row > 1:
                # Eliminate connection upwards
                vertical[row - 2][col - 1] = 0
            if row < rows:
                # Elimiante connection downwards
                vertical[row - 1][col - 1] = 0

    # The connections left are the number of buildings
    print(sum([sum(x) for x in horizontal]) + sum([sum(x) for x in vertical]))

    cols, rows, gaps = [int(x) for x in input().split()]
