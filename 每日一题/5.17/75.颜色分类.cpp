/*
 * @lc app=leetcode.cn id=75 lang=cpp
 *
 * [75] 颜色分类
 */
#include "tools.h"

// @lc code=start
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int cnt0 = 0, cnt01 = 0;
        for (int i = 0; i < nums.size(); i ++ )
        {
            int tmp = nums[i];
            nums[i] = 2;
            if (tmp <= 1) nums[cnt01 ++] = 1;
            if (tmp == 0) nums[cnt0 ++] = 0;
        }
    }
};
// @lc code=end

