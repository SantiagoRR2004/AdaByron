#include <iostream>
using namespace std;

int main()
{
    int nCasos;
    cin >> nCasos;

    for (int i = 0; i < nCasos; ++i)
    {
        int l;
        cin >> l;

        /*
        El número de negras ha sido calculado por partes y
        después se ha simplificado la fórmula.

        Las cuatro esquinas:
            + 4
        Los cuatro lados:
            + 4 * (l - 2)
        El centro:
            + 1
        Lo qe queda de la cruz:
            + 2 * (l - 2)
        */
        int nNegras = 6 * l - 9;
        int nBlancas = l * l - nNegras;
        cout << nNegras << " " << nBlancas << endl;
    }

    return 0;
}
