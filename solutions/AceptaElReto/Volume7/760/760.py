# https://aceptaelreto.com/problem/statement.php?id=760
# https://en.wikipedia.org/wiki/Permutation


MOD = 1_000_000_007


def permutations(nElements: int, minimum: int, maximum: int) -> int:
    current = 1

    # Calculate the number of permutations for the minimum size
    for i in range(minimum):
        current *= nElements - i
        current %= MOD

    total = current

    # Iterate from minimum to maximum - 1
    for i in range(minimum, maximum):
        current *= nElements - i
        current %= MOD
        total += current
        total %= MOD

    return total


nCases = int(input())

for _ in range(nCases):
    length, minimum, maximum = [int(x) for x in input().split()]
    n = length**2

    print(permutations(n, minimum, maximum))

"""
Pista 1
Resolver el problema requiere ciertos conocimientos de combinatoria.

Pista 2
El número de códigos de desbloqueo para un tamaño del código T en una rejilla con P puntos
son las variaciones de P elementos cogidos de T en T.

Pista 3
Las variaciones de P elementos cogidos de T en T son la multiplicación de todos los números entre P y P−T+1.

Pista 4
El resultado puede ser muy grande. Haz el módulo con el número primo del enunciado tras cada operación.

Pista 5
Si calculas las variaciones para cada tamaño de manera independiente tardarás demasiado tiempo.

Pista 6
Las variaciones de P elementos cogidos de T+1 en T+1 se puede calcular muy rápidamente
si conoces las variaciones de P elementos cogidos de T en T.
"""
