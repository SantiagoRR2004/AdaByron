#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <functional>

using namespace std;

class DisjointSet
{
public:
    vector<int> parent;

    DisjointSet(int n)
    {
        parent.resize(n);
        for (int i = 0; i < n; ++i)
            parent[i] = i;
    }

    int find(int u)
    {
        if (parent[u] != u)
            parent[u] = find(parent[u]);
        return parent[u];
    }

    void union_sets(int u, int v)
    {
        int root_u = find(u);
        int root_v = find(v);
        if (root_u != root_v)
            parent[root_v] = root_u;
    }
};

void add_edge(vector<vector<int>> &adjacency, int u, int v)
{
    adjacency[u].push_back(v);
}

bool hasCycle(int nNodes, const vector<vector<int>> &adj)
{
    vector<int> visited(nNodes, 0); // 0 = unvisited, 1 = visiting, 2 = visited

    function<bool(int)> dfs = [&](int node) -> bool
    {
        if (visited[node] == 1)
            return true;
        if (visited[node] == 2)
            return false;

        visited[node] = 1;
        for (int neighbor : adj[node])
        {
            if (dfs(neighbor))
                return true;
        }
        visited[node] = 2;
        return false;
    };

    for (int i = 0; i < nNodes; ++i)
    {
        if (visited[i] == 0)
        {
            if (dfs(i))
                return true;
        }
    }

    return false;
}

int main()
{
    int nParticipantes, nResultados;
    while (cin >> nParticipantes >> nResultados)
    {

        DisjointSet dSet(nParticipantes + 1);
        vector<pair<int, int>> lessThan;

        int p1, p2;
        char op;

        for (int j = 0; j < nResultados; ++j)
        {
            cin >> p1 >> op >> p2;

            if (op == '=')
            {
                dSet.union_sets(p1, p2);
            }
            else if (op == '>')
            {
                lessThan.emplace_back(p2, p1);
            }
            else
            { // <
                lessThan.emplace_back(p1, p2);
            }
        }

        vector<vector<int>> adjacencyList(nParticipantes + 1);
        for (auto &edge : lessThan)
        {
            int root1 = dSet.find(edge.first);
            int root2 = dSet.find(edge.second);
            add_edge(adjacencyList, root1, root2);
        }

        if (hasCycle(nParticipantes + 1, adjacencyList))
        {
            cout << "TRAMPAS" << endl;
        }
        else
        {
            cout << "DESCONFIADO" << endl;
        }
    }

    return 0;
}
