nCases = int(input())

for _ in range(nCases):
    height, width, m, n = [int(x) for x in input().split()]

    maximum = 0
    minimum = 0

    for h in range(height):
        values = [int(x) for x in input().split()]

        if m:
            pass