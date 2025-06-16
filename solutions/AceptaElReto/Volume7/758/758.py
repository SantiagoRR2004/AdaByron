# https://aceptaelreto.com/problem/statement.php?id=758

nCasos = int(input())

for _ in range(nCasos):
    l = int(input())
    """
    El número de negras ha sido calculado por partes y 
    después se ha simplificado la fórmula.
    
    Las cuatro esquinas:
        + 4
    Los cuatro lados:
        + 4 * (l - 2)
    El centro:    
        + 1
    Lo qe queda de la cruz:
        + 2 * (l - 2)
    """
    nNegras = 6 * l - 9
    nBlancas = l**2 - nNegras
    print(nNegras, nBlancas)
