def getNeighbours(h, w) -> list:
    toret = []
    if h < height-1: # Tres de debajo
        if w > 0:
            toret.append([h+1,w-1])
        toret.append([h+1,w])
        if w < width-1:
            toret.append([h+1,w+1])
    if w < width-1: # Dos de la derecha
        if h > 0:
            toret.append([h-1,w+1])
        toret.append([h,w+1])
    if h > 0: # Arriba
        toret.append([h-1,w])
        if w > 0: # Arriba izquierda
            toret.append([h-1,w-1])
    if w > 0: # Izquierda
        toret.append([h,w-1])

    return toret

def recursive(posLand:list) -> None:
    for l in posLand:
        value = matrix[l[0]][l[1]]
        if value == 1:
            matrix[l[0]][l[1]] = 0
            neigh = getNeighbours(l[0],l[1])
            recursive(neigh)


nCases = int(input())

for _ in range(nCases):
    height, width= [int(x) for x in input().split()]

    matrix= []


    for h in range(height):
        matrix.append([int(x) for x in input().split()])


    nIslands = 0

    for h in range(height):
        for w in range(width):
            if matrix[h][w] == 1:
                matrix[h][w] = 0
                nIslands += 1
                neigh = getNeighbours(h,w)
                recursive(neigh)

    print(nIslands)

"""4
5 5
1 1 0 0 0
1 1 0 0 1
0 0 0 1 1
0 0 0 0 0
1 1 0 0 1
6 6
1 1 0 0 1 0
1 1 0 1 1 0
0 0 0 1 1 0
0 1 1 0 0 0
1 1 0 0 1 1
1 1 0 0 1 1
1 1
0
1 3
1 0 1"""