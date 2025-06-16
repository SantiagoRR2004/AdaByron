# https://aceptaelreto.com/problem/statement.php?id=746


n, d = [int(x) for x in input().split()]

while n != 0 and d != 0:

    data = [int(x) for x in input().split()]
    start = 0
    end = len(data) - 1
    numPair = 0
    data.sort()

    while start < end:
        if data[start] + data[end] == d:
            numPair += 1
            start += 1
            end -= 1
        elif data[start] + data[end] < d:
            start += 1
        else:
            end -= 1

    print(numPair)
    n, d = [int(x) for x in input().split()]
