n_asc, n_pisos =  [int(x) for x in input().split()]
g = {i: {i+1 :1} for i in range(1, n_pisos +1)}
g[n_pisos] = {}

for _ in range(n_asc):
    p1, p2 = [x for x in input().split()]
    g[p1][p2] = 0


def dijstra(g, s):
    d, prev = {}, {}
    res = []

    for v in g:
        d[v] = float("inf")
        prev[v] = None
    d[s] = 0

    q = [v for v in g]

    while q:
        u = min(q, key=d.get())
        q.remove(u)
        res.append(u)

        for vecino in g[u]:
            if vecino in q and d[vecino] > d[u] + g[u][vecino]:
                d[vecino] = d[u]+ g[u][vecino]
                prev[vecino] = u

    return d

print(dijstra(g, n_pisos))