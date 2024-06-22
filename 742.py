#  https://aceptaelreto.com/problem/statement.php?id=742

n = int(input())

# Sergey nunca muere entonces estamos siempre en un cero
for i in range(n):
    list1 = [int(x) for x in list(input())]
    randomOnes = list1.count(1)
    ceros = 0
    ones = 0
    for i in range(len(list1)):
        if list1[i - 1] == 0:
            if list1[i] == 0:
                ceros += 1
            else:
                ones += 1

    probTurn = (len(list1) - randomOnes) / len(list1)
    probNoTurn = ceros / (ceros + ones)

    if probNoTurn == probTurn:
        print("Da igual")
    elif probNoTurn > probTurn:
        print("No girar")
    else:
        print("Girar")


"""

#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // Include this for std::count

using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; ++i) {
        string inputStr;
        cin >> inputStr;

        vector<int> list1;
        for (char c : inputStr) {
            list1.push_back(c - '0');
        }

        int randomOnes = count(list1.begin(), list1.end(), 1);
        int ceros = 0;
        int ones = 0;

        for (size_t j = 0; j < list1.size(); ++j) {
            if (list1[(j - 1 + list1.size()) % list1.size()] == 0) {
                if (list1[j] == 0) {
                    ceros += 1;
                } else {
                    ones += 1;
                }
            }
        }

        double probTurn = static_cast<double>(list1.size() - randomOnes) / list1.size();
        double probNoTurn = static_cast<double>(ceros) / (ceros + ones);

        if (probNoTurn == probTurn) {
            cout << "Da igual" << endl;
        } else if (probNoTurn > probTurn) {
            cout << "No girar" << endl;
        } else {
            cout << "Girar" << endl;
        }
    }

    return 0;
}

"""
