#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

double polinomioEsquina(double hallWidthA, double hallWidthB, double objectWidth, double slope)
{
    double aSquared = hallWidthA * hallWidthA;
    double bSquared = hallWidthB * hallWidthB;
    double wSquared = objectWidth * objectWidth;
    double mSquared = slope * slope;
    double mCubed = mSquared * slope;
    double mFourth = mCubed * slope;
    double mSixth = mFourth * mSquared;

    return (bSquared - wSquared) * mSixth + wSquared * mFourth - 2 * hallWidthA * hallWidthB * mCubed + wSquared * mSquared + (aSquared - wSquared);
}

double ajustarPendiente(double comienzo, double fin, double anchoObjeto)
{
    if (comienzo == fin)
    {
        return 1.0;
    }

    double lowerLimit = 0.0;
    double upperLimit = pow(comienzo / fin, 1.0 / 3.0);
    double pendiente = 0.0;

    for (int i = 0; i < 100; ++i)
    {
        pendiente = (lowerLimit + upperLimit) / 2.0;
        double evaluacion = polinomioEsquina(comienzo, fin, anchoObjeto, pendiente);

        if (evaluacion < 0)
        {
            upperLimit = pendiente;
        }
        else
        {
            lowerLimit = pendiente;
        }
    }

    return pendiente;
}

double longitud_max(double ancho1, double ancho2, double anchObjeto, double pendiente)
{
    double angleFactor = 1.0 + 1.0 / (pendiente * pendiente);
    double distanciaEfectiva = pendiente * ancho2 + ancho1 - anchObjeto * sqrt(pendiente * pendiente + 1.0);
    distanciaEfectiva = distanciaEfectiva * distanciaEfectiva;

    return sqrt(angleFactor * distanciaEfectiva);
}

int main()
{
    int anchoPiano, largoPiano, anchoPasillo1, anchoPasillo2;

    while (cin >> anchoPiano >> largoPiano >> anchoPasillo1 >> anchoPasillo2)
    {
        int ladoCorto = min(anchoPiano, largoPiano);
        int ladoLargo = max(anchoPiano, largoPiano);

        if (ladoCorto > anchoPasillo1 || ladoCorto > anchoPasillo2)
        {
            cout << "NO" << endl;
            continue;
        }

        if (anchoPasillo1 > anchoPasillo2)
        {
            swap(anchoPasillo1, anchoPasillo2);
        }

        double slope = ajustarPendiente(anchoPasillo1, anchoPasillo2, ladoCorto);
        double longitudMax = longitud_max(anchoPasillo1, anchoPasillo2, ladoCorto, slope);

        if (ladoLargo <= longitudMax)
        {
            cout << "SI" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }

    return 0;
}
