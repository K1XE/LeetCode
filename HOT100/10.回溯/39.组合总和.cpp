/*
 * @lc app=leetcode.cn id=39 lang=cpp
 *
 * [39] 组合总和
 */
#include "tools.h"

// @lc code=start
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        int n = candidates.size();
        vector<vector<int>> res;
        vector<int> pack;
        auto dfs = [&](auto&& self, int sta) -> void
        {
            if (target == 0)
            {
                res.emplace_back(pack);
                return; 
            }
            for (int i = sta; i < n; i ++ )
            {
                target -= candidates[i];
                if (target < 0)
                {
                    target += candidates[i];
                    break;
                }
                pack.push_back(candidates[i]);
                self(self, i);
                pack.pop_back();
                target += candidates[i];
            }
        };
        ranges::sort(candidates);
        dfs(dfs, 0);
        return res;
    }
};
// @lc code=end

