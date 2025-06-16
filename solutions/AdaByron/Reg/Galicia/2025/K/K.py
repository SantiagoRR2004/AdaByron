nCases = int(input())

for _ in range(nCases):
    number, base = [int(x) for x in input().split()]

    final = ""

    while number >= base:
        div, rest = divmod(number, base)
        final += str(rest)
        number = div

    final += str(number)
    final = final[::-1]


    print(final)