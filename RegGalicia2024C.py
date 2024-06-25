nCasosPrueba = int(input())

for _ in range(nCasosPrueba):
    nCampistas, nAmistades = [int(x) for x in input().split()]
    for _ in range(nAmistades):
        friend1, friend2 = [int(x) for x in input().split()]
