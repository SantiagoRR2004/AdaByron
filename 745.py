# https://aceptaelreto.com/problem/statement.php?id=745


list1 = [int(x) for x in input().split()]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def excelRecursive(n):
    if n <= 0:
        return ""
    n -= 1
    return excelRecursive(n // 26) + alphabet[n % 26]


def decimal_to_base26(decimal):
    if decimal <= 0:
        return ""

    base26 = ""
    while decimal > 0:
        remainder = (decimal - 1) % 26
        base26 = chr(remainder + 65) + base26
        decimal = (decimal - 1) // 26

    return base26


def excelTranslate(n):
    word = ""
    while n > 0:
        n -= 1
        word = alphabet[n % 26] + word
        n //= 26
    return word


while list1[0] != 0:
    list1.pop(-1)
    solution = []
    for code in list1:
        solution.append(excelTranslate(code))

    print(" ".join(solution))
    list1 = [int(x) for x in input().split()]


"""
Pista 1
El proceso es parecido a un cambio de base, donde los "dígitos" son las letras.

Pista 2
La operación módulo (resto) cicla entre 0 y n−1.

Pista 3
Si la letra de más a la derecha del identificador de la columna (la "menos significativa")
cicla entre A y Z, la operación módulo puede ser útil para calcularla.

Pista 4
Para calcular la letra de más a la derecha utiliza el módulo con 26, el número de letras del abecedario inglés. 
Como las columnas se empiezan numerando por la 1 pero el primer módulo es 0, resta 1 antes de calcular el módulo.

Pista 5
"Quita la letra" de más a la derecha del número dividiendo por 26.
Al igual que al calcular la primera letra (de más a la derecha), recuerda restar 1.

Pista 6
Repite el proceso mientras te quede número.
"""
