#https://aceptaelreto.com/problem/statement.php?id=120


n, k = map(int, input().split())

'''Se rellena la mitad de la matriz hasta llegar a la diagonal principal, 
que es la que nos da el resultado de forma más facil'''
while n != 0:
    num_abajo_izquierda = ((n**2 - n) // 2) + k 

    diagonal = [num_abajo_izquierda + i for i in range(0,n)]

    print(sum(diagonal))

    n, k = map(int, input().split())

'''
#include <iostream>
using namespace std;

int main() {

    // mejor std::getline, el tercer parámetro funcioina como split() pero hay pasos extra
    int n, k, num_magico;
    cin >> n >> k;
    /* cout << n << endl;
    cout << k<< endl; */

    while (n != 0) {
    
        int num_abajo_izquierda = (( n*n - n ) / 2) + k;
    
        num_magico = 0;

        for (int i=0; i<n; i++) {
            
            num_magico = num_magico + num_abajo_izquierda++;  
        }

        cout << num_magico << endl;

        cin >> n >> k;
    }
    return 0;

}
'''



