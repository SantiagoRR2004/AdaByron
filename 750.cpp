#include <iostream>
#include <string>

int main()
{
    int n;
    std::cin >> n;

    while (n != 0)
    {
        int numCeros = 0;
        int mult = 1;

        while (n > 9)
        {
            std::string str_n = std::to_string(n);

            for (char c : str_n)
            {
                if (c == '0')
                {
                    numCeros++;
                }
                else
                {
                    mult *= c - '0';
                }
            }

            n = mult;
            mult = 1;
        }

        std::cout << n << numCeros << std::endl;
        std::cin >> n;
    }

    return 0;
}
