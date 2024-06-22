# https://aceptaelreto.com/problem/statement.php?id=105

days = ("MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO")
# datos = [float(x) for x in input().split("\n")]

datos = []
while True:
    inp = float(input())
    if inp != -1:
        datos.append(inp)
    else:
        break

stride = len(days)
aux = []

for i in range(0, len(datos), stride):

    max = [0, 0]  # value and index
    min = [float("inf"), 0]  # value and index
    aux = datos[i : i + stride]

    for i in range(0, len(aux)):
        if aux[i] > max[0]:
            max = [aux[i], days[i]]
        elif aux[i] == max[0]:
            max[1] = "EMPATE"

        if aux[i] < min[0]:
            min = [aux[i], days[i]]
        elif aux[i] == min[0]:
            min[1] = "EMPATE"

    mean = sum(aux) / stride

    if mean < aux[-1]:
        s = "SI"
    else:
        s = "NO"

    print(max[1] + " " + min[1] + " " + s)

"""

#include <iostream>
#include <vector>
#include <string>
#include <limits> // Para std::numeric_limits

int main() {
    std::vector<std::string> days = {"MARTES", "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"};
    std::vector<float> datos;
    float inp;

    // Leer datos hasta que se ingrese -1
    while (std::cin >> inp && inp != -1) {
        datos.push_back(inp);
    }

    int stride = days.size();
    std::vector<float> aux;

    for (size_t i = 0; i < datos.size(); i += stride) {
        float maxVal = 0;
        std::string maxDay = "";
        float minVal = std::numeric_limits<float>::infinity();
        std::string minDay = "";
        aux.clear();

        for (size_t j = i; j < i + stride && j < datos.size(); ++j) {
            aux.push_back(datos[j]);
        }

        for (size_t j = 0; j < aux.size(); ++j) {
            if (aux[j] > maxVal) {
                maxVal = aux[j];
                maxDay = days[j];
            } else if (aux[j] == maxVal) {
                maxDay = "EMPATE";
            }

            if (aux[j] < minVal) {
                minVal = aux[j];
                minDay = days[j];
            } else if (aux[j] == minVal) {
                minDay = "EMPATE";
            }
        }

        float sum = 0;
        for (float value : aux) {
            sum += value;
        }
        float mean = sum / stride;

        std::string s = (mean < aux.back()) ? "SI" : "NO";

        std::cout << maxDay << " " << minDay << " " << s << std::endl;
    }

    return 0;
}

"""
