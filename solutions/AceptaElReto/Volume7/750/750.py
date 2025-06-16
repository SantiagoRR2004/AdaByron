# https://aceptaelreto.com/problem/statement.php?id=750


n = int(input())

while n != 0:

    numCeros = 0
    mult = 1
    while n > 9:
        for i in str(n):
            if i == "0":
                numCeros += 1
            else:
                mult *= int(i)
        n = mult
        mult = 1

    print(f"{n}{numCeros}")
    n = int(input())
