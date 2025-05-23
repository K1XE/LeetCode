/*
 * @lc app=leetcode.cn id=55 lang=cpp
 *
 * [55] 跳跃游戏
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int co = nums[0];
        for (int i = 0; i <= co; i ++ )
        {
            co = max(co, i + nums[i]);
            if (i >= nums.size() - 1) return 1;
        }
        return 0;
    }
};
// @lc code=end

