#include <iostream>
using namespace std;

const int MOD = 1000000007;

long long permutations(int nElements, int minimum, int maximum)
{
    long long current = 1;

    // Calculate the number of permutations for the minimum size
    for (int i = 0; i < minimum; ++i)
    {
        current *= (nElements - i);
        current %= MOD;
    }

    long long total = current;

    // Iterate from minimum to maximum - 1
    for (int i = minimum; i < maximum; ++i)
    {
        current *= (nElements - i);
        current %= MOD;
        total += current;
        total %= MOD;
    }

    return total;
}

int main()
{
    int nCases;
    cin >> nCases;

    for (int i = 0; i < nCases; ++i)
    {
        int length, minimum, maximum;
        cin >> length >> minimum >> maximum;

        int n = length * length;
        cout << permutations(n, minimum, maximum) << endl;
    }

    return 0;
}
