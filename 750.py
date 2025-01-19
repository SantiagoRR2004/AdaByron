# https://aceptaelreto.com/problem/statement.php?id=750


n = int(input())

while n != 0:

    numCeros = 0
    mult = 1
    while n > 9:
        for i in str(n):
            if i == "0":
                numCeros += 1
            else:
                mult *= int(i)
        n = mult
        mult = 1

    print(f"{n}{numCeros}")
    n = int(input())


"""

#include <iostream>
#include <string>

int main() {
    int n;
    std::cin >> n;

    while (n != 0) {
        int numCeros = 0;
        int mult = 1;

        while (n > 9) {
            std::string str_n = std::to_string(n);

            for (char c : str_n) {
                if (c == '0') {
                    numCeros++;
                } else {
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

"""
