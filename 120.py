# https://aceptaelreto.com/problem/statement.php?id=120


n, k = map(int, input().split())

"""Se rellena la mitad de la matriz hasta llegar a la diagonal principal, 
que es la que nos da el resultado de forma más facil"""
while n != 0:
    num_abajo_izquierda = ((n**2 - n) // 2) + k

    diagonal = [num_abajo_izquierda + i for i in range(0, n)]

    print(sum(diagonal))

    n, k = map(int, input().split())
