# Accepted

n = int(input())

for _ in range(n):
    nmagos = int(input())
    sabidu = [int(x) for x in input().split()]

    sorted = sabidu.copy()
    sorted.sort()
    winner = sorted[0]
    sum = sorted[0]
    sorted.pop(0)

    for index, value in enumerate(sorted):
        if sum >= sorted[-1]:
            break
        if sum < value:
            winner = value
        sum += value

    print(sabidu.index(winner) + 1)
