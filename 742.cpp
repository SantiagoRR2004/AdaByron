#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // Include this for std::count

using namespace std;

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; ++i)
    {
        string inputStr;
        cin >> inputStr;

        vector<int> list1;
        for (char c : inputStr)
        {
            list1.push_back(c - '0');
        }

        int randomOnes = count(list1.begin(), list1.end(), 1);
        int ceros = 0;
        int ones = 0;

        for (size_t j = 0; j < list1.size(); ++j)
        {
            if (list1[(j - 1 + list1.size()) % list1.size()] == 0)
            {
                if (list1[j] == 0)
                {
                    ceros += 1;
                }
                else
                {
                    ones += 1;
                }
            }
        }

        double probTurn = static_cast<double>(list1.size() - randomOnes) / list1.size();
        double probNoTurn = static_cast<double>(ceros) / (ceros + ones);

        if (probNoTurn == probTurn)
        {
            cout << "Da igual" << endl;
        }
        else if (probNoTurn > probTurn)
        {
            cout << "No girar" << endl;
        }
        else
        {
            cout << "Girar" << endl;
        }
    }

    return 0;
}
