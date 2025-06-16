# https://aceptaelreto.com/problem/statement.php?id=745


def excelTranslate(n):
    word = ""
    while n > 0:
        n -= 1
        word = chr(ord('A') + n % 26) + word
        n //= 26
    return word


import sys

first = True

while True:
    # Iterate this way to reduce memory usage
    n = ""
    while True:
        char = sys.stdin.read(1)
        if char == " " or char == "\n" or not char:
            break
        n += char

    if n == "0":
        if not first:
            print()
        else:
            break
        first = True
    else:
        if not first:
            print(" ", end="")
        print(excelTranslate(int(n)), end="")
        first = False


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
