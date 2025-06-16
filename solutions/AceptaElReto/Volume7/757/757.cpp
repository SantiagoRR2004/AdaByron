#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    int nCasos;
    std::cin >> nCasos;
    std::cin.ignore(); // to ignore the newline character after reading nCasos

    for (int i = 0; i < nCasos; ++i)
    {
        std::string cadena;
        std::getline(std::cin, cadena);

        std::vector<int> lengths;
        size_t start = 0;
        size_t end;
        while ((end = cadena.find('S', start)) != std::string::npos)
        {
            lengths.push_back(end - start);
            start = end + 1;
        }
        lengths.push_back(cadena.length() - start); // last segment after the last 'S'

        int maxLength = *std::max_element(lengths.begin(), lengths.end());
        std::cout << maxLength << std::endl;
    }

    return 0;
}
