#include <iostream>
using namespace std;

int main()
{

    // mejor std::getline, el tercer parámetro funcioina como split() pero hay pasos extra
    int n, k, num_magico;
    cin >> n >> k;
    /* cout << n << endl;
    cout << k<< endl; */

    while (n != 0)
    {

        int num_abajo_izquierda = ((n * n - n) / 2) + k;

        num_magico = 0;

        for (int i = 0; i < n; i++)
        {

            num_magico = num_magico + num_abajo_izquierda++;
        }

        cout << num_magico << endl;

        cin >> n >> k;
    }
    return 0;
}
