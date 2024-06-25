# https://en.wikipedia.org/wiki/Bipartite_graph#Testing_bipartiteness

nCasos = int(input())

for _ in range(nCasos):

    nAmigos, nRivalidades = [int(x) for x in input().split()]

    for _ in range(nRivalidades):
        per1, per2 = [int(x) for x in input().split()]
