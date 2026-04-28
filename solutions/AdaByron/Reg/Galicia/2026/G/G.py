nCases = int(input())

for _ in range(nCases):
    toret = ""

    for i in list(input()):

        if len(toret) and i == toret[-1]:
            toret = toret[:-1]
        else:
            toret += i

    if not toret:
        print(0)
    else:
        print(toret)
