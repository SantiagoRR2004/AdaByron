#  https://aceptaelreto.com/problem/statement.php?id=742

n = int(input())

# Sergey nunca muere entonces estamos siempre en un cero
for i in range(n):
    list1 = [int(x) for x in list(input())]
    randomOnes = list1.count(1)
    ceros = 0
    ones = 0
    for i in range(len(list1)):
        if list1[i - 1] == 0:
            if list1[i] == 0:
                ceros += 1
            else:
                ones += 1

    probTurn = (len(list1) - randomOnes) / len(list1)
    probNoTurn = ceros / (ceros + ones)

    if probNoTurn == probTurn:
        print("Da igual")
    elif probNoTurn > probTurn:
        print("No girar")
    else:
        print("Girar")

