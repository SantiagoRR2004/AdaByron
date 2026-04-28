# Greedy
nCases = int(input())

for _ in range(nCases):
    nDesks, nTeams, k = [int(x) for x in input().split()]

    monitoring = k * 2

    desks = [int(x) for x in input().split()]

    desks.sort()

    limit = desks[0] + monitoring

    result = 1

    for i in desks:

        if i > limit:
            result += 1
            limit = i + monitoring

    print(result)
