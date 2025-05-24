/*
 * @lc app=leetcode.cn id=1005 lang=cpp
 *
 * [1005] K 次取反后最大化的数组和
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    static bool cmp(int a, int b)
    {
        return abs(a) > abs(b);
    }
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        ranges::sort(nums, cmp);
        int res = 0;
        for (int i = 0; i < nums.size(); i ++ )
        {
            if (nums[i] < 0 && k > 0)
            {
                nums[i] *= -1;
                k --;
            }
            if (i < nums.size() - 1) res += nums[i];
        }
        if (k % 2) nums[nums.size() - 1] *= -1;
        return res + nums.back();
    }
};
// @lc code=end

