# https://aceptaelreto.com/problem/statement.php?id=759


class Node:
    def __init__(self):
        self.moreThan = set()
        self.lessThan = set()

    def addMoreThan(self, node) -> bool:
        if node in self.lessThan or self == node:
            return False

        self.moreThan.add(node)
        return True

    def addLessThan(self, node) -> bool:
        if node in self.moreThan or self == node:
            return False

        self.lessThan.add(node)
        return True

    def equals(self, node):
        if node in self.moreThan or node in self.lessThan:
            return False
        newNode = Node()
        newNode.moreThan = self.moreThan.union(node.moreThan)
        newNode.lessThan = self.lessThan.union(node.lessThan)

        return newNode


def hasCycle(nodes):
    visited = [False] * len(nodes)
    recStack = [False] * len(nodes)

    def dfs(node):
        if not visited[node]:
            visited[node] = True
            recStack[node] = True

            # Recursively visit all neighbors
            for neighbor in nodes[node].moreThan:
                if not visited[nodes.index(neighbor)]:
                    if dfs(nodes.index(neighbor)):
                        return True
                elif recStack[nodes.index(neighbor)]:
                    return True

            # Backtrack: remove the node from recursion stack
            recStack[node] = False

        return False

    # Check for cycle in each node
    for node in range(len(nodes)):
        if dfs(node):
            return True

    return False


import sys

data = sys.stdin.readlines()
i = 0

while i < len(data):
    nParticipantes, nResultados = [int(x) for x in data[i].strip().split()]
    participants = [Node() for _ in range(nParticipantes)]
    i += 1
    cheaterFlag = False

    for j in range(nResultados):
        p1, op, p2 = data[i].strip().split()
        i += 1
        if not cheaterFlag:
            if "=" == op:
                newNode = participants[int(p1) - 1].equals(participants[int(p2) - 1])
                if newNode:
                    participants[int(p1) - 1] = newNode
                    participants[int(p2) - 1] = newNode
                else:
                    print("TRAMPAS")
                    cheaterFlag = True
            elif ">" == op:
                if not participants[int(p2) - 1].addMoreThan(
                    participants[int(p1) - 1]
                ) or not participants[int(p1) - 1].addLessThan(
                    participants[int(p2) - 1]
                ):
                    print("TRAMPAS")
                    cheaterFlag = True
            else:
                if not participants[int(p1) - 1].addMoreThan(
                    participants[int(p2) - 1]
                ) or not participants[int(p2) - 1].addLessThan(
                    participants[int(p1) - 1]
                ):
                    print("TRAMPAS")
                    cheaterFlag = True

    if not cheaterFlag:
        participants = list(set(participants))
        # Now we check for a loop
        if hasCycle(participants):
            print("TRAMPAS")
        else:
            print("DESCONFIADO")
