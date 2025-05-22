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
        int res = INT_MIN, tmp = 0;
        for (int i = 0; i < n; i ++ )
        {
            tmp += nums[i];
            res = max(tmp, res);
            if (tmp <= 0) tmp = 0;
        }
        return res;
    }
};
// @lc code=end

