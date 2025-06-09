#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main()
{
    int nOperation;
    cin >> nOperation;

    while (nOperation > 0)
    {
        unordered_map<string, int> cowboys;
        for (int i = 0; i < nOperation; ++i)
        {
            string operation;
            cin >> operation;
            if (operation == "?")
            {
                int exits, guns = 0;
                cin >> exits;
                for (int j = 0; j < exits; ++j)
                {
                    string cowboy;
                    cin >> cowboy;
                    if (cowboys.find(cowboy) != cowboys.end())
                    {
                        guns += cowboys[cowboy];
                        cowboys.erase(cowboy);
                    }
                }
                cout << guns << endl;
            }
            else
            {
                int amount;
                cin >> amount;
                if (cowboys.find(operation) != cowboys.end())
                {
                    cowboys[operation] += amount;
                }
                else
                {
                    cowboys[operation] = amount;
                }
            }
        }
        cout << "---" << endl;
        cin >> nOperation;
    }

    return 0;
}
