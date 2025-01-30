# https://en.wikipedia.org/wiki/Bipartite_graph#Testing_bipartiteness


def depthFirstSearch(rivalidades, inicial) -> bool:

    if visitados[inicial - 1]:
        return True

    if equipos[inicial - 1] == -1:
        # No importa el equipo
        equipos[inicial - 1] = 0

    visitados[inicial - 1] = True

    for rival in rivalidades[inicial]:
        # Es imposible que se puedan dividir los equipos
        if equipos[rival - 1] == equipos[inicial - 1]:
            return False

        # Si no se ha visitado, se asigna el equipo contrario
        if not visitados[rival - 1]:
            equipos[rival - 1] = 1 - equipos[inicial - 1]

    # Ahora se recorre a los rivales
    for rival in rivalidades[inicial]:
        # Si no se puede dividir, se retorna False
        if not depthFirstSearch(rivalidades, rival):
            return False

    # Hay que comprobar que todos estén en un equipo
    for i in range(len(visitados)):
        if not visitados[i]:
            if not depthFirstSearch(rivalidades, i + 1):
                return False

    return True


nCasos = int(input())

for _ in range(nCasos):

    nAmigos, nRivalidades = [int(x) for x in input().split()]

    rivalidades = {x: [] for x in range(1, nAmigos + 1)}

    for _ in range(nRivalidades):
        per1, per2 = [int(x) for x in input().split()]

        rivalidades[per1].append(per2)
        rivalidades[per2].append(per1)

    # Estar en el -1 es no estar en ningun equipo
    equipos = [-1 for _ in range(nAmigos)]

    visitados = [False for _ in range(nAmigos)]

    if depthFirstSearch(rivalidades, 1):
        print("Que comience la batalla")
    else:
        print("Mejor nos vamos de cena o algo")
