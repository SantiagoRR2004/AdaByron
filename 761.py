# https://aceptaelreto.com/problem/statement.php?id=761
# https://es.wikipedia.org/wiki/Algoritmo_de_Bellman-Ford


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []  # List of edges

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def remove_edges(self, u):
        # Removes all edges that start at u
        self.edges = [edge for edge in self.edges if edge[0] != u]

    def bellman_ford(self, src):
        # Step 1: Initialize distances from src to all other vertices as INFINITE
        dist = [float("inf")] * self.V
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Check for negative-weight cycles
        for u, v, w in self.edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                return None

        return dist[self.V - 1]


import sys

data = sys.stdin.readlines()
index = 0

while index < len(data):
    columns, rows = [int(x) for x in data[index].strip().split()]
    index += 1

    matrix = []
    graph = Graph(columns * rows)
    wormholePositions = []

    # Store the map
    for i in range(rows):
        row = list(data[index].strip())
        matrix.append(row)
        index += 1

    # First, connect all valid adjacent cells
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == "#":
                continue  # Wall, no connections
            u = i * columns + j
            # Check 4 directions
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < rows and 0 <= nj < columns and matrix[ni][nj] != "#":
                    v = ni * columns + nj
                    graph.add_edge(u, v, 1)

            if matrix[i][j] == "O":
                wormholePositions.append(u)
                # Remove current outgoing edges (to simulate teleport)
                graph.remove_edges(u)

    for i in range(len(wormholePositions)):
        # col, row, value
        wormholeData = [int(x) for x in data[index].strip().split()]
        graph.add_edge(
            wormholePositions[i],
            (wormholeData[1] - 1) * columns + (wormholeData[0] - 1),
            wormholeData[2],
        )
        index += 1

    # Remove edges from the objective
    graph.remove_edges((rows - 1) * columns + (columns - 1))

    result = graph.bellman_ford(0)

    if result is None:
        print("EXPLOSION")
    elif result == float("inf"):
        print("IMPOSIBLE")
    else:
        print(result)

"""
Pista 1
Piensa cómo resolverías el problema si los agujeros de gusano nunca recargaran
la nave y por tanto no pudiera ocurrir el caso EXPLOSION.

Pista 2
El problema se puede modelizar como un grafo dirigido,
donde muchas aristas son implícitas, generadas por la vecindad de las celdas en el mapa.

Pista 3
Si los agujeros de gusano siempre consumieran energía,
el problema se podría resolver con el algoritmo de Dijkstra para
buscar el camino mínimo entre el origen y el destino.

Pista 4
El algoritmo de Dijkstra no funciona bien si hay aristas con pesos negativos.
Busca una alternativa.

Pista 5
El algoritmo de Bellman–Ford calcula el camino más corto desde un 
vértice de un grafo dirigido a todos los demás, 
y soporta la existencia de aristas con pesos negativos.
Permite además detectar la existencia de ciclos negativos
que hacen que no haya un camino más corto porque éste puede
siempre reducirse dando una vuelta más al ciclo.

Pista 6
Usa el algoritmo de Bellman-Ford para calcular el camino mínimo
y detectar si hay algún ciclo negativo. Si lo hay, escribe EXPLOSION.

Pista 7
Para que Jessy caiga en un ciclo negativo y haga explotar las 
baterías de su nave tiene que poder llegar a él. 
No siempre que hay un ciclo negativo hay que escribir EXPLOSION.
"""
