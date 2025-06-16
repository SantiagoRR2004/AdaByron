# https://aceptaelreto.com/problem/statement.php?id=757

nCasos = int(input())

for _ in range(nCasos):
    cadena = input()
    cadenas = cadena.split("S")
    print(max([len(c) for c in cadenas]))
