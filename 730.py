# https://aceptaelreto.com/problem/statement.php?id=730

casos = int(input())

datos = []
for i in range(0, casos):
    inp = int(input())
    datos.append(inp)

# Versión 1

for n in datos:

    digits = 0

    if n == 0:
        print(digits)
    elif n == 1:
        print(digits + 1)
    else:

        coc = n // 2
        if n % 2:
            digits += 1
        n = coc

        while coc != 1:

            coc = n // 2
            if n % 2:
                digits += 1
            n = coc

        digits += 1

        print(digits)

# Versión 2
# Otra opción, auque esta la busqué en internet después
"""for n in datos:
    print(format(n, '08b').count('1'))"""
