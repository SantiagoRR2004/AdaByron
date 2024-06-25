# https://aceptaelreto.com/problem/statement.php?id=753
# https://es.wikipedia.org/wiki/Problema_de_la_partici%C3%B3n
# https://en.wikipedia.org/wiki/Knapsack_problem


def can_partition_TLE(nums):

    # No consideramos el caso en que la suma de los elementos es impar
    # porque el enunciado dice que siempre será par

    target = sum(nums) // 2
    n = len(nums)

    # Crear un conjunto para almacenar las sumas alcanzables
    achievable_sums = {0}

    for num in nums:
        new_sums = set()
        for s in achievable_sums:
            if s + num == target:
                return True
            new_sums.add(s + num)
        achievable_sums.update(new_sums)

    return target in achievable_sums


def can_partition_MLE(nums):

    # No consideramos el caso en que la suma de los elementos es impar
    # porque el enunciado dice que siempre será par

    target = sum(nums) // 2
    n = len(nums)

    # Crear una tabla DP para almacenar si es posible alcanzar cada suma desde 0 hasta target
    dp = [False] * (target + 1)
    dp[0] = True  # Siempre podemos obtener una suma de 0

    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[target]


nStones = int(input())


while nStones != 0:

    stones = [int(x) for x in input().split()]

    if can_partition_TLE(stones):
        print("SI")
    else:
        print("NO")

    nStones = int(input())
