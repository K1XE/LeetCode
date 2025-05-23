/*
 * @lc app=leetcode.cn id=45 lang=cpp
 *
 * [45] 跳跃游戏 II
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    int jump(vector<int>& nums) {
        int nxt = 0, res = 0, ends = 0;
        for (int i = 0; i < nums.size(); i ++ )
        {
            nxt = max(nxt, i + nums[i]);
            if (i == ends)
            {
                if (ends < nums.size() - 1)
                {
                    ends = nxt;
                    res ++;
                }
                if (ends >= nums.size() - 1) break;
            }
        }
        return res;
    }
};
// @lc code=end

