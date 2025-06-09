#include <iostream>
#include <vector>
#include <sstream>

int main()
{
    std::string line;
    while (std::getline(std::cin, line))
    {
        int inversiones = 0;

        std::vector<int> piezas;
        std::stringstream ss(line);
        int num;

        while (ss >> num)
        {
            piezas.push_back(num);
        }

        for (size_t i = 0; i < piezas.size(); ++i)
        {
            for (size_t j = i + 1; j < piezas.size(); ++j)
            {
                if (piezas[i] > piezas[j])
                {
                    ++inversiones;
                }
            }
        }

        if (inversiones % 2 == 0)
        {
            std::cout << "SI" << std::endl;
        }
        else
        {
            std::cout << "NO" << std::endl;
        }
    }

    return 0;
}
