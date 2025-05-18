#include "tools.h"
class Solution {
    public:
        int minSwaps(vector<int>& nums) {
            vector<int> tmp;
            for (int i = 0; i < nums.size(); i ++ )
            {
                tmp.push_back(solve(nums[i]));
            }
            int n = tmp.size();
            vector<pair<pair<int, int>, int>> tmp_pos(n);
            vector<bool> vis(n, 0);
            for (int i = 0; i < n; i ++ ) tmp_pos[i] = {{tmp[i], nums[i]}, i};

            ranges::sort(tmp_pos.begin(), tmp_pos.end());
            int res = 0;
            for (int i = 0; i < n; i ++ )
            {
                if (vis[i] || tmp_pos[i].second == i) continue;
                int csize = 0;
                int j = i;
                while (! vis[j])
                {
                    vis[j] = 1;
                    j = tmp_pos[j].second;
                    csize ++;
                }
                if (csize > 0) res += csize - 1;
            }
            return res;
        }
        long long solve(int x)
        {
            long long res = 0;
            while (x)
            {
                res += x % 10;
                x /= 10;
            }
            return res;
        }
    };