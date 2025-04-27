#include <bits/stdc++.h>
#include <ranges>
using namespace std;
class Solution {
    public:
        vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
            vector<bool> res(queries.size(), 0);
            for (int i = 0; i < queries.size(); i ++ )
            {
                int a = queries[i][0], b = queries[i][1];
                if (abs(nums[a] - nums[b]) <= maxDiff) res[i] = 1; 
                else
                {
                    bool flag = 1;
                    int l = b, r = a;
                    if (l < r) swap(l, r);
                    for (int u = l; u > r; u -- )
                    {
                        if (abs(nums[u] - nums[u - 1]) <= maxDiff) continue;
                        else flag = 0;
                    }
                    if (flag) res[i] = 1;
                }
            }
            return res;
        }

    };