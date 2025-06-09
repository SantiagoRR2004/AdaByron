#include <iostream>
#include <unordered_map>
#include <string>
#include <algorithm>
#include <vector>


int main()
{
    std::string line;

    while (std::getline(std::cin, line))
    {
        std::unordered_map<char, int> letters;

        for (char letter : line)
        {
            if (letter != ' ')
            {
                letters[letter]++;
            }
        }

        int numberOfOdds = 0;
        for (const auto &pair : letters)
        {
            if (pair.second % 2 != 0)
            {
                numberOfOdds++;
            }
        }

        if (numberOfOdds > 1)
        {
            std::cout << "NO HAY" << std::endl;
        }
        else
        {
            std::string solution = "";
            std::string middle = "";

            std::vector<char> sortedLetters;
            for (const auto &pair : letters)
            {
                sortedLetters.push_back(pair.first);
            }
            std::sort(sortedLetters.rbegin(), sortedLetters.rend());

            for (char letter : sortedLetters)
            {
                solution = std::string(letters[letter] / 2, letter) + solution + std::string(letters[letter] / 2, letter);
                if (letters[letter] % 2 != 0)
                {
                    middle = letter;
                }
            }

            solution.insert(solution.begin() + solution.size() / 2, middle.begin(), middle.end());

            std::cout << solution << std::endl;
        }
    }

    return 0;
}
