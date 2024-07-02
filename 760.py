# https://aceptaelreto.com/problem/statement.php?id=760
# https://en.wikipedia.org/wiki/Permutation
# https://es.wikipedia.org/wiki/Inverso_multiplicativo_(aritm%C3%A9tica_modular)

# MOD = 1_000_000_007
# def factorial(n, cache={}):
#     if n not in cache:
#         cache[n] = n * factorial(n - 1, fact_cache)
#     return cache[n]
# def permutations(n, r, cache={}):
#     return (factorial(n, cache) // factorial(n - r, cache)) % MOD
# nCases = int(input())
# fact_cache = {0: 1}
# for _ in range(nCases):
#     length, minimum, maximum = [int(x) for x in input().split()]
#     n = length**2
#     total = 0
#     for i in range(minimum, maximum + 1):
#         total += permutations(n, i, fact_cache) % MOD
#     print(total % MOD)


MOD = 1_000_000_007


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def permutations(n, r):
    return (factorial(n) // factorial(n - r)) % MOD


nCases = int(input())

for _ in range(nCases):
    length, minimum, maximum = [int(x) for x in input().split()]
    n = length**2

    total = 0

    for i in range(minimum, maximum + 1):
        total += permutations(n, i) % MOD

    print(total % MOD)
