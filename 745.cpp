#include <iostream>
#include <string>

std::string excelTranslate(unsigned long long n)
{
    std::string word = "";
    while (n > 0)
    {
        n -= 1;
        char c = 'A' + (n % 26);
        word = c + word;
        n /= 26;
    }
    return word;
}

int main()
{
    bool first = true;
    while (true)
    {
        std::string n_str;
        char ch;

        // Read until space, newline or EOF
        while (std::cin.get(ch))
        {
            if (ch == ' ' || ch == '\n')
                break;
            n_str += ch;
        }

        if (n_str.empty())
        {
            // If input ended without reading a number
            break;
        }

        if (n_str == "0")
        {
            if (!first)
            {
                std::cout << std::endl;
            }
            else
            {
                break;
            }
            first = true;
        }
        else
        {
            // Convert string to unsigned long long
            unsigned long long n = 0;
            for (char digit : n_str)
            {
                n = n * 10 + (digit - '0');
            }

            if (!first)
            {
                std::cout << " ";
            }
            std::cout << excelTranslate(n);
            first = false;
        }
    }
    return 0;
}
