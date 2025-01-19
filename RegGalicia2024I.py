n = int(input())


while n != 0:

    data = [int(x) for x in input().split()]
    result = [1 for x in range(len(data))]

    for i in range(1, len(data)):
        b = i - 1
        while data[i] >= data[b] and b >= 0:
            result[i] += result[b]
            b -= result[b]

    print(" ".join([str(x) for x in result]))

    n = int(input())
