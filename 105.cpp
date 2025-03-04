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