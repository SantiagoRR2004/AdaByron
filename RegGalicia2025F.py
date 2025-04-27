nCases = int(input())

for _ in range(nCases):
    nStreams, nTime = [int(x) for x in input().split()]

    times = [int(x) for x in input().split()]
    valoresAbs = [int(x) for x in input().split()]


    vs = [v/t for v,t in zip(valoresAbs,times)]
    ind = {}
    for i in range(nStreams):
        ind[times[i]] = i

    ind2 = {}
    for i in range(nStreams):
        ind2[valoresAbs[i]] = i

    times.sort(key=lambda k:vs[ind[k]],reverse=True)
    valoresAbs.sort(key=lambda k:vs[ind2[k]],reverse=True)
    vs.sort(reverse=True)

    value = 0

    counter = 0
    while nTime != 0 and counter < nStreams:
        maxTime = min(nTime, times[counter])

        value += maxTime*valoresAbs[counter]/times[counter]
        nTime -= maxTime

        counter += 1

    print(f"{round(value,4):.4f}")


"""3
4 125
16 27 38 41
30 75 105 180
5 67
11 22 31 41 54
25 60 90 120 200
3 5
12 24 36
47 97 140
"""