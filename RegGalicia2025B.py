
def recursive(set1, number, maximun) -> int:

    if len(set1)+number <= maximun:
        return number
    
    for c in set1:
        inter = clases[c]["noCoin"].intersection(set1)
        number = max(number, recursive(inter, number+1, maximun))

    return number


nClases = int(input())

clases = {}

for _ in range(nClases):
    classN, start, end = [x for x in input().split()]
    start = int(start)
    end = int(end)

    clases[classN] = {"s": start, "e":end, "noCoin":set()}

    for c in clases.keys():
        if (clases[c]["s"] > clases[classN]["e"]) or\
            (clases[c]["e"] < clases[classN]["s"]):
            clases[c]["noCoin"].add(classN)

maximun = 1
counter = 0

for c in clases.keys():
    
    if nClases - counter <= maximun:
        break

    counter += 1

    for c2 in clases[c]["noCoin"]:
        inter = clases[c]["noCoin"].intersection(clases[c2]["noCoin"])
        maximun = max(maximun, recursive(inter, 2, maximun))

print(maximun)