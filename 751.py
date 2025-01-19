# https://aceptaelreto.com/problem/statement.php?id=751

n = int(input())


for _ in range(n):
    start1, end1, start2, end2 = [int(x) for x in input().split()]

    start = max(start1, start2)
    end = min(end1, end2)

    if start <= end:
        print(end - start + 1)
    else:
        print(0)

"""

#include <iostream>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;

    for (int i = 0; i < n; ++i) {
        int start1, end1, start2, end2;
        std::cin >> start1 >> end1 >> start2 >> end2;

        int start = std::max(start1, start2);
        int end = std::min(end1, end2);

        if (start <= end) {
            std::cout << (end - start + 1) << std::endl;
        } else {
            std::cout << 0 << std::endl;
        }
    }

    return 0;
}

"""
