numCromos, numSobres, precioSobre = [int(x) for x in input().split()]

preciosCromo = [int(x) for x in input().split()]

sobres = [
    [int(x) for x in input().split()] 
    for _ in range(numSobres)
    ]

faltantes = [True] * numCromos
valSobres = 0
resultados = []

for i in range(numSobres):
    valSobres += precioSobre

    for cromo in sobres[i]:
        faltantes[cromo-1] = False

    valFaltantes = sum([j for idx, j in enumerate(preciosCromo) if faltantes[idx]])

    resultados.append(valSobres + valFaltantes)

print(min(resultados))