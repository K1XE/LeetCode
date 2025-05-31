/*
 * @lc app=leetcode.cn id=2094 lang=cpp
 *
 * [2094] 找出 3 位偶数
 */
#include "tools.h"
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        ranges::sort(digits);
        vector<int> res, pack;
        int n = digits.size();
        vector<bool> vis(n, 0);
        auto check = [&](vector<int>& pack) -> bool
        {
            return !(pack.back() % 2) && pack[0] != 0;
        };
        auto solve = [&](vector<int> pack) -> int
        {
            return pack[0] * 100 + pack[1] * 10 + pack[2];
        };

        auto dfs = [&](auto&& self, vector<bool>& vis, vector<int>& pack) -> void
        {
            if (pack.size() == 3)
            {
                if (check(pack)) res.push_back(solve(pack));
                return;
            }
            for (int i = 0; i < n; i ++ )
            {
                if (vis[i] == 1) continue;
                if (i > 0 && digits[i] == digits[i - 1] && !vis[i - 1]) continue;
                vis[i] = 1;
                pack.push_back(digits[i]);
                self(self, vis, pack);
                pack.pop_back();
                vis[i] = 0;
            }
        };
        
        dfs(dfs, vis, pack);
        return res;
    }
};
// @lc code=end

