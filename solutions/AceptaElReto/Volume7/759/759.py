# https://aceptaelreto.com/problem/statement.php?id=759
# https://en.wikipedia.org/wiki/Disjoint-set_data_structure


class DisjointSet:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u


def add_edge(adyacencia: list[list[int]], u: int, v: int) -> None:
    adyacencia[u].append(v)


def hasCycle(nNodes: int, adj: list[list[int]]) -> bool:
    visited = [0] * nNodes  # 0 = unvisited, 1 = visiting, 2 = visited

    def dfs(node):
        if visited[node] == 1:
            return True
        if visited[node] == 2:
            return False

        visited[node] = 1  # mark as visiting
        for neighbor in adj[node]:
            if dfs(neighbor):
                return True
        visited[node] = 2
        return False

    for i in range(nNodes):
        if visited[i] == 0:
            if dfs(i):
                return True

    return False


import sys

inputIterator = iter(sys.stdin)

while True:
    try:
        line = next(inputIterator).strip()
        if not line:
            continue
        nParticipantes, nResultados = [int(x) for x in line.split()]
    except StopIteration:
        break  # No more input
    except ValueError:
        continue  # Skip invalid lines

    dSet = DisjointSet(nParticipantes + 1)

    lessThan = []

    for j in range(nResultados):
        p1, op, p2 = next(inputIterator).strip().split()

        
        if "=" == op:
            # The participants are equal
            dSet.union(int(p1), int(p2))
        elif ">" == op:
            lessThan.append((int(p2), int(p1)))
        else:
            lessThan.append((int(p1), int(p2)))

    adjacencyList = [[] for _ in range(nParticipantes + 1)]
    for op1, op2 in lessThan:
        root1 = dSet.find(op1)
        root2 = dSet.find(op2)
        add_edge(adjacencyList, root1, root2)

    if hasCycle(nParticipantes + 1, adjacencyList):
        print("TRAMPAS")
    else:
        print("DESCONFIADO")


"""
Pista 1
Si nadie hace trampa, hay un único orden entre los participantes, 
aunque es posible que no podamos conocerlo entero si nos faltan resultados comparados en la entrada.

Pista 2
Si no tenemos todos los resultados, la información que tenemos de los partipantes crea un orden parcial, 
donde podremos decir en algunos casos que un participante es mejor que otro, pero no siempre.

Pista 3
Un orden parcial se puede representar con un grafo dirigido acíclico (DAG, por sus siglas en inglés).

Pista 4
Tenemos confirmación de que alguien hace trampa si usando la información del orden parcial 
podemos demostrar que un participante A es mejor que otro participante B y, al mismo tiempo, que B es mejor que A.

Pista 5
Si alguien hace trampas no tendremos un orden parcial y en el grafo habrá al menos un ciclo.

Pista 6
Construye un grafo dirigido donde los nodos representen a los participantes y cada arista 
indique que el participante asociado al nodo origen es mejor que el participante destino.
Busca ciclos en el grafo para decidir qué contestar.

Pista 7
Los participantes que empaten son iguales en el orden parcial. Representalos en el grafo como un único nodo.

Pista 8
Antes de crear el grafo, agrupa a los participantes que empaten entre sí.
Puedes utilizar la estructura de conjuntos disjuntos (union-find disjoint sets, UFDS)
para tener un nodo representante de cada grupo y usarlo como origen y destino de todas las aristas de los nodos que representa.
"""
