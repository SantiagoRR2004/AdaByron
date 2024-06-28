# https://aceptaelreto.com/problem/statement.php?id=756

import sys

for line in sys.stdin:
    inversiones = 0

    piezas = [int(num) for num in line.split()]

    for i in range(len(piezas)):
        for j in range(i + 1, len(piezas)):
            if piezas[i] > piezas[j]:
                inversiones += 1

    if inversiones % 2 == 0:
        print("SI")
    else:
        print("NO")

"""

#include <iostream>
#include <vector>
#include <sstream>

int main() {
    std::string line;
    while (std::getline(std::cin, line)) {
        int inversiones = 0;

        std::vector<int> piezas;
        std::stringstream ss(line);
        int num;

        while (ss >> num) {
            piezas.push_back(num);
        }

        for (size_t i = 0; i < piezas.size(); ++i) {
            for (size_t j = i + 1; j < piezas.size(); ++j) {
                if (piezas[i] > piezas[j]) {
                    ++inversiones;
                }
            }
        }

        if (inversiones % 2 == 0) {
            std::cout << "SI" << std::endl;
        } else {
            std::cout << "NO" << std::endl;
        }
    }

    return 0;
}

"""
