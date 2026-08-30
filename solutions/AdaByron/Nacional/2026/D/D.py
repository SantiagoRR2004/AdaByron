nCases = int(input())

for _ in range(nCases):
    nDeliveries = int(input())

    deliv = [0] + [int(x) for x in input().split()] + [0]

    currentMax = 0
    currentLength = abs(deliv[0] - deliv[1])

    for i in range(1, len(deliv) - 1):

        newLength = abs(deliv[i] - deliv[i - 1]) + abs(deliv[i] - deliv[i + 1])
        skipped = newLength - abs(deliv[i - 1] - deliv[i + 1])

        if skipped > currentMax:
            currentLength += (
                currentMax
                + abs(deliv[i - 1] - deliv[i + 1])
                - abs(deliv[i] - deliv[i - 1])
            )
            currentMax = skipped
        else:
            currentLength += abs(deliv[i] - deliv[i + 1])

    print(currentLength)
