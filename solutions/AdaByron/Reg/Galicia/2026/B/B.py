from collections import Counter


palabras = input().split()

freq = Counter(palabras)
sortedFreq = freq.most_common(2)


if len(sortedFreq) >= 2:
    if sortedFreq[0][1] == sortedFreq[1][1]:
        print("empate")
    else:
        print(sortedFreq[0][0])
else:
    print(sortedFreq[0][0])
