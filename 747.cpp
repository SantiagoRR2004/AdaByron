#include <iostream>
#include <vector>
#include <queue>
#include <set>

using namespace std;

bool is_path_exists(const vector<vector<int>> &matrix)
{
    int rows = matrix.size();
    int cols = matrix[0].size();
    if (matrix[0][0] != 0 || matrix[rows - 1][cols - 1] != 0)
    {
        return false;
    }

    // Directions for moving up, down, left, right
    vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    // Initialize queue with the starting position and mark it as visited
    queue<pair<int, int>> q;
    q.push({0, 0});
    set<pair<int, int>> visited;
    visited.insert({0, 0});

    while (!q.empty())
    {
        pair<int, int> current = q.front();
        q.pop();

        int x = current.first;
        int y = current.second;

        if (x == rows - 1 && y == cols - 1)
        {
            return true;
        }

        for (const auto &dir : directions)
        {
            int nx = x + dir.first;
            int ny = y + dir.second;
            if (0 <= nx && nx < rows && 0 <= ny && ny < cols && matrix[nx][ny] == 0 && visited.find({nx, ny}) == visited.end())
            {
                q.push({nx, ny});
                visited.insert({nx, ny});
            }
        }
    }

    return false;
}

int main()
{
    int rows, cols;
    cin >> rows >> cols;

    while (rows != 0 && cols != 0)
    {
        vector<vector<int>> matrix(rows, vector<int>(cols));
        for (int i = 0; i < rows; ++i)
        {
            string line;
            cin >> line;
            for (int j = 0; j < cols; ++j)
            {
                if (line[j] == '.')
                {
                    matrix[i][j] = 0;
                }
                else
                {
                    matrix[i][j] = 1;
                }
            }
        }

        if (is_path_exists(matrix))
        {
            cout << "SI" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }

        cin >> rows >> cols;
    }

    return 0;
}
