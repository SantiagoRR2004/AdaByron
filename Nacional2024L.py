# Time limit exceeded

import sys

data = sys.stdin.readlines()
# data = """5 6
# 1 2 1
# 1 4 5
# 3 2 4
# 4 5 5
# 5 2 10
# 5 3 8
# 4 2
# 3 1
# 2 3 10
# 1 2""".split("\n")


def dijstra(graph, entry, out, maxNodes):
    visited = [False] * maxNodes
    anchos = [-1] * maxNodes

    anchos[entry - 1] = float("inf")
    visited[entry - 1] = True

    if not graph.get(entry):
        return 0

    nexts = list(graph[entry].keys())

    for n in nexts:
        anchos[n - 1] = graph[entry][n]

    while nexts:
        next = max(nexts, key=lambda k: anchos)
        if next == out:
            break
        visited[next - 1] = True
        nexts.remove(next)

        if graph.get(next):
            newNodes = list(graph[next].keys())

            for n in newNodes:
                if not visited[n - 1]:
                    anchos[n - 1] = max(
                        min(graph[next][n], anchos[next - 1]), anchos[n - 1]
                    )
                    nexts.append(n)

    return anchos[out - 1]


index = 0


while index < len(data):
    nodes, conecc = [int(x) for x in data[index].strip().split()]
    index += 1

    graph = {}

    inverse = {x + 1: set() for x in range(nodes)}

    for _ in range(conecc):
        from1, to, girth = [int(x) for x in data[index].strip().split()]
        index += 1
        if graph.get(from1):
            graph[from1][to] = girth
        else:
            graph[from1] = {to: girth}

        inverse[to].add(from1)

    origin, obj = [int(x) for x in data[index].strip().split()]
    index += 1

    visited = [False] * nodes
    visited[obj - 1] = True

    nexts = inverse[obj]

    while nexts:
        n = nexts.pop()
        visited[n - 1] = True
        nexts = nexts.union(set([x for x in inverse[n] if not visited[x - 1]]))

    for i in range(len(visited)):
        if not visited[i] and graph.get(i + 1):
            del graph[i + 1]

    print(dijstra(graph, origin, obj, nodes))
