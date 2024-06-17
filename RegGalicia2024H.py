# https://stackoverflow.com/questions/76270040/solving-algorithm-for-a-rotating-pipes-game
filas, columnas = [int(x) for x in input().split()]

while filas != 0 and columnas != 0:

    matrix = []
    for i in range(filas):
        data = input().split()
        row = []
        for number in data:
            if number == "x":
                row.append(0)
            else:
                row.append(len(number))
        matrix.append(row)

    print(matrix)
    filas, columnas = [int(x) for x in input().split()]
