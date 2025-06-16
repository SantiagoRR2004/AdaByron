def getNeighbours(h, w, height, width):
    toret = []
    if h < height - 1:  # Tres de debajo
        if w > 0:
            toret.append([h + 1, w - 1])
        toret.append([h + 1, w])
        if w < width - 1:
            toret.append([h + 1, w + 1])
    if w < width - 1:  # Dos de la derecha
        if h > 0:
            toret.append([h - 1, w + 1])
        toret.append([h, w + 1])
    if h > 0:  # Arriba
        toret.append([h - 1, w])
        if w > 0:  # Arriba izquierda
            toret.append([h - 1, w - 1])
    if w > 0:  # Izquierda
        toret.append([h, w - 1])

    return toret


def dfs(h, w, height, width, matrix):
    stack = [(h, w)]
    while stack:
        x, y = stack.pop()
        if matrix[x][y] == 1:
            matrix[x][y] = 0  # Marcar como visitado
            for nx, ny in getNeighbours(x, y, height, width):
                if matrix[nx][ny] == 1:
                    stack.append((nx, ny))


nCases = int(input())
for _ in range(nCases):
    height, width = [int(x) for x in input().split()]

    matrix = []

    for h in range(height):
        matrix.append([int(x) for x in input().split()])

    nIslands = 0
    for h in range(height):
        for w in range(width):
            if matrix[h][w] == 1:
                dfs(h, w, height, width, matrix)
                nIslands += 1

    print(nIslands)
