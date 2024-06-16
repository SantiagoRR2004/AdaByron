#  https://aceptaelreto.com/problem/statement.php?id=742

n = int(input())

# Sergey nunca muere entonces estamos siempre en un cero
for i in range(n):
    list1 = [int(x) for x in list(input())]
    ceros = 0
    ones = 0
    for i in range(len(list1)):
        if list1[i-1] == 0:
            if list1[i] == 0:
                ceros += 1
            else:
                ones += 1
    if ceros == ones:
        print("Da igual")
    elif ceros > ones:
        print("No girar")
    else:
        print("Girar")
