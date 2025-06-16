# https://aceptaelreto.com/problem/statement.php?id=105

days = ("MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO")
# datos = [float(x) for x in input().split("\n")]

datos = []
while True:
    inp = float(input())
    if inp != -1:
        datos.append(inp)
    else:
        break

stride = len(days)
aux = []

for i in range(0, len(datos), stride):

    max = [0, 0]  # value and index
    min = [float("inf"), 0]  # value and index
    aux = datos[i : i + stride]

    for i in range(0, len(aux)):
        if aux[i] > max[0]:
            max = [aux[i], days[i]]
        elif aux[i] == max[0]:
            max[1] = "EMPATE"

        if aux[i] < min[0]:
            min = [aux[i], days[i]]
        elif aux[i] == min[0]:
            min[1] = "EMPATE"

    mean = sum(aux) / stride

    if mean < aux[-1]:
        s = "SI"
    else:
        s = "NO"

    print(max[1] + " " + min[1] + " " + s)
