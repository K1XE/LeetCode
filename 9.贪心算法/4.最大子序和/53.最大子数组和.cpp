/*
 * @lc app=leetcode.cn id=53 lang=cpp
 *
 * [53] 最大子数组和
 */
#include "tools.h"

// @lc code=start
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int maxS = nums[0], cur = nums[0];
        for (int i = 1; i < n; i ++ )
        {
            cur = max(nums[i], cur + nums[i]);
            maxS = max(cur, maxS);
        }
        return maxS;
    }
};
// @lc code=end

