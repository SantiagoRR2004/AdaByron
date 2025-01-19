# https://aceptaelreto.com/problem/statement.php?id=748

nOperation = int(input())

while nOperation > 0:
    cowboys = {}
    for _ in range(nOperation):
        operation = input().split()
        if operation[0] == "?":
            exits = int(operation[1])
            guns = 0
            for i in range(2, 2 + exits):
                if operation[i] in cowboys.keys():
                    guns += cowboys[operation[i]]
                    cowboys.pop(operation[i])
            print(guns)
        else:
            if operation[0] in cowboys.keys():
                cowboys[operation[0]] += int(operation[1])
            else:
                cowboys[operation[0]] = int(operation[1])

    print("---")
    nOperation = int(input())


"""
#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main() {
    int nOperation;
    cin >> nOperation;

    while (nOperation > 0) {
        unordered_map<string, int> cowboys;
        for (int i = 0; i < nOperation; ++i) {
            string operation;
            cin >> operation;
            if (operation == "?") {
                int exits, guns = 0;
                cin >> exits;
                for (int j = 0; j < exits; ++j) {
                    string cowboy;
                    cin >> cowboy;
                    if (cowboys.find(cowboy) != cowboys.end()) {
                        guns += cowboys[cowboy];
                        cowboys.erase(cowboy);
                    }
                }
                cout << guns << endl;
            } else {
                int amount;
                cin >> amount;
                if (cowboys.find(operation) != cowboys.end()) {
                    cowboys[operation] += amount;
                } else {
                    cowboys[operation] = amount;
                }
            }
        }
        cout << "---" << endl;
        cin >> nOperation;
    }

    return 0;
}

"""
