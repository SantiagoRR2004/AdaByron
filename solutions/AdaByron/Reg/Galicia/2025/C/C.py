currentBest = float("inf")


def search(current: int, end: int, notVisited: set, distance: float) -> int:
    """
    Perform a DFS to find the shortest path from the start to the end.
    """
    global currentBest

    if distance >= currentBest:
        return float("inf")

    if not notVisited:
        finalDistance = distance + graph[current]["out"].get(end, float("inf"))
        if finalDistance < currentBest:
            currentBest = finalDistance
        return finalDistance

    minDistance = float("inf")

    for neighbor in graph[current]["out"]:
        if neighbor in notVisited:
            newDistance = search(
                neighbor,
                end,
                notVisited - {neighbor},
                distance + graph[current]["out"][neighbor],
            )
            if newDistance < minDistance:
                minDistance = newDistance

    return minDistance


nPlaces, nEdges = [int(x) for x in input().split()]

graph = {x + 1: {"out": {}, "in": {}} for x in range(nPlaces)}

for _ in range(nEdges):
    origin, destination, duration = [int(x) for x in input().split()]
    graph[origin]["out"][destination] = min(
        duration, graph[origin]["out"].get(destination, float("inf"))
    )
    graph[destination]["in"][origin] = min(
        duration, graph[destination]["in"].get(origin, float("inf"))
    )

start, end, nWaypoints = [int(x) for x in input().split()]

waypoints = [int(input()) for _ in range(nWaypoints)]
notImportant = [
    x for x in range(1, nPlaces + 1) if x not in waypoints and x != start and x != end
]

# Eliminate in from start and out from end
for neighbor in graph[start]["in"]:
    del graph[neighbor]["out"][start]
graph[start]["in"] = {}

for neighbor in graph[end]["out"]:
    del graph[neighbor]["in"][end]
graph[end]["out"] = {}

for x in notImportant:
    for exiting in graph[x]["out"].keys():
        for entering in graph[x]["in"].keys():
            if exiting == entering:
                continue
            newDistance = min(
                graph[entering]["out"].get(exiting, float("inf")),
                graph[entering]["out"][x] + graph[x]["out"][exiting],
            )
            graph[entering]["out"][exiting] = newDistance
            graph[exiting]["in"][entering] = newDistance

    # Delete x from the graph
    # Delete node x from the graph completely
    for neighbor in graph[x]["out"]:
        del graph[neighbor]["in"][x]
    for neighbor in graph[x]["in"]:
        del graph[neighbor]["out"][x]
    del graph[x]


print(search(start, end, set(waypoints), 0))
