#include <iostream>
#include <vector>
#include <numeric> // for accumulate

using namespace std;

bool can(const vector<int> &nums, int index, int suma, int target)
{
    if (suma == target)
    {
        return true;
    }
    if (suma > target || index == (int)nums.size())
    {
        return false;
    }

    int tempSum = suma;
    for (int i = index; i < (int)nums.size(); ++i)
    {
        tempSum += nums[i];
        if (tempSum > suma)
        {
            break;
        }
        if (tempSum == suma)
        {
            return true;
        }
    }

    return can(nums, index + 1, suma + nums[index], target) || can(nums, index + 1, suma, target);
}

int main()
{
    int nStones;
    while (cin >> nStones && nStones != 0)
    {
        vector<int> stones(nStones);
        for (int i = 0; i < nStones; ++i)
        {
            cin >> stones[i];
        }

        int suma = accumulate(stones.begin(), stones.end(), 0);

        if (can(stones, 0, 0, suma / 2))
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
