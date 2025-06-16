#include <iostream>
#include <algorithm>

int main()
{
    int n;
    std::cin >> n;

    for (int i = 0; i < n; ++i)
    {
        int start1, end1, start2, end2;
        std::cin >> start1 >> end1 >> start2 >> end2;

        int start = std::max(start1, start2);
        int end = std::min(end1, end2);

        if (start <= end)
        {
            std::cout << (end - start + 1) << std::endl;
        }
        else
        {
            std::cout << 0 << std::endl;
        }
    }

    return 0;
}