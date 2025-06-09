# https://aceptaelreto.com/problem/statement.php?id=755
# https://es.wikipedia.org/wiki/Algoritmo_de_Euclides
# https://en.wikipedia.org/wiki/Euclidean_algorithm


def euclideanAlgorithm(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


nCases = int(input())

for _ in range(nCases):
    num1, num2 = [int(x) for x in input().split()]
    MCD = euclideanAlgorithm(num1, num2)
    print(num1 * num2 // MCD**2)
