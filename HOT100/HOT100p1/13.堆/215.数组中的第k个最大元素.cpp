/*
 * @lc app=leetcode.cn id=215 lang=cpp
 *
 * [215] 数组中的第K个最大元素
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
        auto dfs = [&](auto&& self, vector<int>& nums, int k) -> int
        {
            vector<int> l, m, r;
            int piv = nums[rand() % nums.size()];
            for (auto x : nums)
            {
                if (x > piv) r.push_back(x);
                else if (x == piv) m.push_back(x);
                else l.push_back(x);
            }
            if (k <= r.size()) return self(self, r, k);
            if (k > r.size() + m.size()) return self(self, l, k - (r.size() + m.size()));
            return piv;
        };

        return dfs(dfs, nums, k);
    }
};
// @lc code=end

