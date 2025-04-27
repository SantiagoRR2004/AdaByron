nCases = int(input())

for _ in range(nCases):
    nCoins = int(input())
    coins = [int(x) for x in input().split()]
    nCursed = int(input())
    listCursed = set([int(x) for x in input().split()])

    sum1 = [x for x in coins if x not in listCursed]

    print(sum(sum1))
