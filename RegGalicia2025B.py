# https://en.wikipedia.org/wiki/Interval_scheduling#Unweighted


nClases = int(input())

clases = {}

for _ in range(nClases):
    classN, start, end = [x for x in input().split()]
    start = int(start)
    end = int(end)

    clases[classN] = {"s": start, "e": end}

nMaxClases = 0

while len(clases) > 0:
    # Get the class with the earliest end time
    clase = min(clases.items(), key=lambda x: x[1]["e"])
    nMaxClases += 1

    # Remove all classes that overlap with the selected class
    clases = {k: v for k, v in clases.items() if v["s"] >= clase[1]["e"]}

print(nMaxClases)
