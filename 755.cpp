#include <iostream>

using namespace std;

long long euclideanAlgorithm(long long num1, long long num2)
{
    while (num2 != 0)
    {
        long long temp = num2;
        num2 = num1 % num2;
        num1 = temp;
    }
    return num1;
}

int main()
{
    int nCases;
    cin >> nCases;

    for (int i = 0; i < nCases; ++i)
    {
        long long num1, num2;
        cin >> num1 >> num2;
        long long MCD = euclideanAlgorithm(num1, num2);
        long long num_parcels = (num1 / MCD) * (num2 / MCD);
        cout << num_parcels << endl;
    }

    return 0;
}
