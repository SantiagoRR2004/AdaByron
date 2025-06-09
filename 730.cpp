#include <iostream>
#include <vector>

int main()
{
    int casos;
    std::cin >> casos; // Leer el número de casos

    std::vector<int> datos(casos);
    for (int i = 0; i < casos; ++i)
    {
        std::cin >> datos[i]; // Leer cada caso
    }

    for (int n : datos)
    {
        int digits = 0;

        if (n == 0)
        {
            std::cout << digits << std::endl;
        }
        else if (n == 1)
        {
            std::cout << digits + 1 << std::endl;
        }
        else
        {
            int coc = n / 2;
            if (n % 2)
            {
                digits += 1;
            }
            n = coc;

            while (coc != 1)
            {
                coc = n / 2;
                if (n % 2)
                {
                    digits += 1;
                }
                n = coc;
            }

            digits += 1;

            std::cout << digits << std::endl;
        }
    }

    return 0;
}

// Versión 2
// Otra opción, auque esta la busqué en internet después

/*
#include <iostream>
#include <bitset>
#include <vector>

int main() {
    int casos;
    std::cin >> casos;

    std::vector<int> datos(casos);
    for (int i = 0; i < casos; ++i) {
        std::cin >> datos[i];
    }

    for (int n : datos) {
        // Convertir el número a una representación binaria de 32 bits porque con 8 y 16 hay overflow
        std::bitset<32> bits(n);
        std::cout << bits.count() << std::endl; // Contar número de bits establecidos a 1
    }

    return 0;
}
*/
