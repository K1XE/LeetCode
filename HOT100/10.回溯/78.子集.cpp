/*
 * @lc app=leetcode.cn id=78 lang=cpp
 *
 * [78] 子集
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        auto dfs = [&](auto&& self, int sta, vector<vector<int>>& res, vector<int>& pack) -> void
        {
            res.emplace_back(pack);
            for (int i = sta; i < n; i ++ )
            {
                pack.push_back(nums[i]);
                self(self, i + 1, res, pack);
                pack.pop_back();
            }
        };
        vector<vector<int>> res;
        vector<int> pack;
        dfs(dfs, 0, res, pack);
        return res;
    }
};
// @lc code=end

