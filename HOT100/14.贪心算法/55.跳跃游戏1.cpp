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
        int n = nums.size();
        for (int i = 0; i <= co; i ++ )
        {
            co = max(i + nums[i], co);
            if (co >= n - 1) return 1;
        }
        return 0;
    }
};
// @lc code=end

