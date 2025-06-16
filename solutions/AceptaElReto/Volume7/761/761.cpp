#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <limits>
#include <tuple>

using namespace std;

class Graph
{
public:
    int V;
    vector<tuple<int, int, int>> edges;

    Graph(int vertices)
    {
        V = vertices;
    }

    void add_edge(int u, int v, int w)
    {
        edges.emplace_back(u, v, w);
    }

    void remove_edges(int u)
    {
        vector<tuple<int, int, int>> filtered;
        for (auto &edge : edges)
        {
            if (get<0>(edge) != u)
            {
                filtered.push_back(edge);
            }
        }
        edges = move(filtered);
    }

    pair<bool, int> bellman_ford(int src)
    {
        vector<int> dist(V, numeric_limits<int>::max());
        dist[src] = 0;

        for (int i = 0; i < V - 1; ++i)
        {
            for (const auto &edge : edges)
            {
                int u, v, w;
                tie(u, v, w) = edge;
                if (dist[u] != numeric_limits<int>::max() && dist[u] + w < dist[v])
                {
                    dist[v] = dist[u] + w;
                }
            }
        }

        for (const auto &edge : edges)
        {
            int u, v, w;
            tie(u, v, w) = edge;
            if (dist[u] != numeric_limits<int>::max() && dist[u] + w < dist[v])
            {
                return {false, 0}; // Negative cycle detected
            }
        }

        int target = V - 1;
        return {true, dist[target]};
    }
};

int main()
{
    string line;
    vector<string> data;
    while (getline(cin, line))
    {
        data.push_back(line);
    }

    size_t index = 0;

    while (index < data.size())
    {
        int columns, rows;
        {
            istringstream ss(data[index++]);
            ss >> columns >> rows;
        }

        vector<string> matrix;
        Graph graph(columns * rows);
        vector<int> wormholePositions;

        for (int i = 0; i < rows; ++i)
        {
            matrix.push_back(data[index++]);
        }

        for (int i = 0; i < rows; ++i)
        {
            for (int j = 0; j < columns; ++j)
            {
                if (matrix[i][j] == '#')
                    continue;

                int u = i * columns + j;

                // Connect to adjacent non-wall cells
                vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
                for (size_t d = 0; d < directions.size(); ++d)
                {
                    int dx = directions[d].first;
                    int dy = directions[d].second;

                    int ni = i + dx;
                    int nj = j + dy;
                    if (ni >= 0 && ni < rows && nj >= 0 && nj < columns && matrix[ni][nj] != '#')
                    {
                        int v = ni * columns + nj;
                        graph.add_edge(u, v, 1);
                    }
                }

                if (matrix[i][j] == 'O')
                {
                    wormholePositions.push_back(u);
                    graph.remove_edges(u);
                }
            }
        }

        for (int i = 0; i < wormholePositions.size(); ++i)
        {
            int col, row, val;
            istringstream ss(data[index++]);
            ss >> col >> row >> val;
            int dest = (row - 1) * columns + (col - 1);
            graph.add_edge(wormholePositions[i], dest, val);
        }

        // Remove edges from the exit node
        graph.remove_edges((rows - 1) * columns + (columns - 1));

        auto result = graph.bellman_ford(0);
        if (!result.first)
        {
            cout << "EXPLOSION" << endl;
        }
        else if (result.second == numeric_limits<int>::max())
        {
            cout << "IMPOSIBLE" << endl;
        }
        else
        {
            cout << result.second << endl;
        }
    }

    return 0;
}
