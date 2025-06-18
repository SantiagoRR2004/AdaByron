numCromos, numSobres, precioSobre = [int(x) for x in input().split()]

preciosCromo = [int(x) for x in input().split()]


precioMin = min(precioSobre * numSobres, sum(preciosCromo))
cromosObtenidos = set()


for i in range(numSobres):
    cromos = [int(x) for x in input().split()]
    cromosObtenidos.update(cromos)
    costoSobres = (i + 1) * precioSobre
    costoCromos = sum(
        preciosCromo[cromo - 1]
        for cromo in (set(range(1, numCromos + 1)) - cromosObtenidos)
    )
    precioMin = min(precioMin, costoSobres + costoCromos)

print(precioMin)


# sobres = [[int(x) for x in input().split()] for _ in range(numSobres)]

# faltantes = [True] * numCromos
# valSobres = 0
# resultados = []

# for i in range(numSobres):
#     valSobres += precioSobre

#     for cromo in sobres[i]:
#         faltantes[cromo - 1] = False

#     valFaltantes = sum([j for idx, j in enumerate(preciosCromo) if faltantes[idx]])

#     resultados.append(valSobres + valFaltantes)

# print(min(resultados))
