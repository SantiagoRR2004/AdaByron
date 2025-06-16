#include <iostream>
#include <set>
#include <vector>

int main()
{
    int cols, rows, gaps;

    while (std::cin >> cols >> rows >> gaps, cols != 0 && rows != 0)
    {
        long long horizontalTotal = (static_cast<long long>(cols - 1)) * static_cast<long long>(rows);
        long long verticalTotal = (static_cast<long long>(rows - 1)) * static_cast<long long>(cols);

        std::set<std::pair<int, int>> horizontalSet;
        std::set<std::pair<int, int>> verticalSet;

        if (gaps > 0)
        {
            std::vector<int> intersections(2 * gaps);
            for (int i = 0; i < 2 * gaps; ++i)
            {
                std::cin >> intersections[i];
            }

            for (int i = 0; i < 2 * gaps; i += 2)
            {
                int x = intersections[i];
                int y = intersections[i + 1];

                // Add top
                verticalSet.emplace(x, std::max(y - 1, 1));
                // Add bottom
                verticalSet.emplace(x, std::min(y, rows - 1));
                // Add left
                horizontalSet.emplace(std::max(x - 1, 1), y);
                // Add right
                horizontalSet.emplace(std::min(x, cols - 1), y);
            }
        }

        std::cout << (horizontalTotal + verticalTotal - horizontalSet.size() - verticalSet.size()) << "\n";
    }

    return 0;
}
