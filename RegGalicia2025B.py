# https://en.wikipedia.org/wiki/Interval_scheduling#Unweighted


nClases = int(input())

clases = []

for _ in range(nClases):
    classN, start, end = input().split()
    start = int(start)
    end = int(end)

    clases.append((start, end))

# Sort classes by end time
clases.sort(key=lambda x: x[1])

nMaxClases = 0
currentEnd = -1

for start, end in clases:
    if start >= currentEnd:
        nMaxClases += 1
        currentEnd = end

print(nMaxClases)
