numCromos, numSobres, precioSobre = [int(x) for x in input().split()]


preciosCromo = [0] + [int(x) for x in input().split()]


faltantes = sum(preciosCromo)
visto = [False] * (numCromos + 1)

precioMin = faltantes

for i in range(1, numSobres + 1):
    sobre = map(int, input().split())

    for cromo in sobre:
        if not visto[cromo]:
            visto[cromo] = True
            faltantes -= preciosCromo[cromo]

    precioMin = min(precioMin, i * precioSobre + faltantes)

print(precioMin)
