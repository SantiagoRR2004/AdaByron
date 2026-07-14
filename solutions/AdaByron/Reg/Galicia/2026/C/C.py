from collections import defaultdict
import queue

rooms, connec, nPortals = [int(x) for x in input().split()]


mainPortals = {n + 1: None for n in range(nPortals)}
portalRedirections = {}

for i, typePortal in enumerate(input().split()):
    intP = int(typePortal)
    if intP > 0:
        if not mainPortals.get(intP):
            mainPortals[intP] = i + 1
        else:
            portalRedirections[i + 1] = mainPortals[intP]

graph = defaultdict(list)

for _ in range(connec):
    a, b = [int(x) for x in input().split()]

    a = portalRedirections.get(a, a)
    b = portalRedirections.get(b, b)

    graph[a].append(b)
    graph[b].append(a)


objective = portalRedirections.get(rooms, rooms)

distances = {1: 0}
futures = queue.Queue()
futures.put((1, 0))
seen = {1}

while objective not in distances and not futures.empty():
    newN, dist = futures.get()

    distances[newN] = dist

    for n in graph.get(newN, []):
        if n not in seen:
            futures.put((n, dist + 1))
            seen.add(n)

if distances.get(objective) or objective == 1:
    print(distances[objective])
else:
    print(-1)
