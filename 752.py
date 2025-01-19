# https://aceptaelreto.com/problem/statement.php?id=752
# https://es.wikipedia.org/wiki/Ventana_deslizante

nPersons, nWagons = [int(x) for x in input().split()]

while nPersons != 0 and nWagons != 0:
    freeSpace = [int(x) for x in input().split()]

    if sum(freeSpace) < nPersons:
        print("NO ENTRAN")
    else:
        best_start = -1
        min_length = nWagons + 1

        current_sum = 0
        start = 0

        for end in range(nWagons):
            current_sum += freeSpace[end]

            while current_sum >= nPersons:
                if (end - start + 1) < min_length:
                    min_length = end - start + 1
                    best_start = start + 1  # Convert to 1-based index

                current_sum -= freeSpace[start]
                start += 1
        print(min_length, best_start)

    nPersons, nWagons = [int(x) for x in input().split()]


"""

#include <iostream>
#include <vector>
#include <numeric> // for accumulate
using namespace std;

int main() {
    int nPersons, nWagons;
    cin >> nPersons >> nWagons;

    while (nPersons != 0 && nWagons != 0) {
        vector<int> freeSpace(nWagons);
        for (int i = 0; i < nWagons; ++i) {
            cin >> freeSpace[i];
        }

        if (accumulate(freeSpace.begin(), freeSpace.end(), 0) < nPersons) {
            cout << "NO ENTRAN" << endl;
        } else {
            int best_start = -1;
            int min_length = nWagons + 1;

            int current_sum = 0;
            int start = 0;

            for (int end = 0; end < nWagons; ++end) {
                current_sum += freeSpace[end];

                while (current_sum >= nPersons) {
                    if ((end - start + 1) < min_length) {
                        min_length = (end - start + 1);
                        best_start = start + 1; // Convert to 1-based index
                    }

                    current_sum -= freeSpace[start];
                    ++start;
                }
            }
            cout << min_length << " " << best_start << endl;
        }

        cin >> nPersons >> nWagons;
    }

    return 0;
}

"""
