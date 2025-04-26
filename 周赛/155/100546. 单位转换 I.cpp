#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Solution {
    public:
        int MOD = 1e9 + 7;
        vector<int> baseUnitConversions(vector<vector<int>>& conversions) {
            vector<int> res(conversions.size() + 1);
            res[0] = 1;
            for (int i = 0; i < conversions.size(); i ++ )
            {
                long long tmp = (long long)res[conversions[i][0]] * conversions[i][2];
                res[conversions[i][1]] = tmp % MOD;
            }
            return res;
        }
    };