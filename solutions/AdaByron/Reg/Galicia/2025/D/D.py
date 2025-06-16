# https://cp-algorithms.com/graph/01_bfs.html


n_asc, n_pisos = [int(x) for x in input().split()]
g = {i: {i + 1: 1} for i in range(1, n_pisos + 1)}
g[n_pisos] = {}

for _ in range(n_asc):
    p1, p2 = [int(x) for x in input().split()]
    g[p1][p2] = 0


def BFS01(g):
    from collections import deque

    goal = len(g)
    queue = deque([1])
    dist = {node: float("inf") for node in g}
    dist[1] = 0

    while queue:
        node = queue.popleft()
        if node == goal:
            return dist[goal]
        for neighbor, weight in g[node].items():
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                if weight == 1:
                    queue.append(neighbor)
                else:
                    queue.appendleft(neighbor)


print(BFS01(g))
