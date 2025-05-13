/*
 * @lc app=leetcode.cn id=46 lang=cpp
 *
 * [46] 全排列
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();

        auto dfs = [&](auto&& self, vector<bool>& vis, vector<vector<int>>& res, vector<int>& pack) -> void
        {
            if (pack.size() == n)
            {
                res.emplace_back(pack);
                return;
            }
            for (int i = 0; i < n; i ++ )
            {
                if (vis[i] == 1) continue;
                vis[i] = 1;
                pack.push_back(nums[i]);
                self(self, vis, res, pack);
                pack.pop_back();
                vis[i] = 0;
            }
        };
        vector<bool> vis(n, 0);
        vector<vector<int>> res;
        vector<int> pack;
        dfs(dfs, vis, res, pack);
        return res;
    }
};
// @lc code=end

