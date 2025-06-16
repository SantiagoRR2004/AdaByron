rows, cols = [int(x) for x in input().split()]


accumulativeMatrix = [[0 for x in range(cols)] for y in range(rows)]

for i in range(rows):
    row = [int(x) for x in input().split()]

    for j in range(cols):
        accumulativeMatrix[i][j] = row[j]
        if i > 0:
            accumulativeMatrix[i][j] += accumulativeMatrix[i - 1][j]
        if j > 0:
            accumulativeMatrix[i][j] += accumulativeMatrix[i][j - 1]
        if i > 0 and j > 0:
            accumulativeMatrix[i][j] -= accumulativeMatrix[i - 1][j - 1]

nCases = int(input())


bestId = 0
bestSum = 0

for _ in range(nCases):
    id, x1, y1, x2, y2 = [int(x) for x in input().split()]
    x1 -= 1  # Convert to zero-based index
    y1 -= 1  # Convert to zero-based index
    x2 -= 1  # Convert to zero-based index
    y2 -= 1  # Convert to zero-based index

    sum = accumulativeMatrix[x2][y2]
    if x1 > 0:
        sum -= accumulativeMatrix[x1 - 1][y2]
    if y1 > 0:
        sum -= accumulativeMatrix[x2][y1 - 1]
    if x1 > 0 and y1 > 0:
        sum += accumulativeMatrix[x1 - 1][y1 - 1]

    if sum > bestSum or (sum == bestSum and id < bestId):
        bestId = id
        bestSum = sum


print(bestId, bestSum)
