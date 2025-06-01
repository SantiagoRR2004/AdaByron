# https://en.wikipedia.org/wiki/Continuous_knapsack_problem

nCases = int(input())

for _ in range(nCases):
    nStreams, nTime = [int(x) for x in input().split()]

    times = [int(x) for x in input().split()]
    valoresAbs = [int(x) for x in input().split()]

    activities = sorted(  # value by time, time and popularity
        [(valoresAbs[i] / times[i], times[i], valoresAbs[i]) for i in range(nStreams)],
        reverse=True,
    )

    totalValue = 0

    for ratio, duration, activityValue in activities:
        if nTime >= duration:
            totalValue += activityValue
            nTime -= duration
        else:
            totalValue += ratio * nTime
            break

    print(f"{totalValue:.4f}")
