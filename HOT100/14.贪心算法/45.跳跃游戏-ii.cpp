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
        int cur_co = 0;
        int nxt_co = 0;
        int res = 0;
        if (nums.size() == 1) return 0;
        for (int i = 0; i < nums.size(); i ++ )
        {
            nxt_co = max(nxt_co, i + nums[i]);
            if (i == cur_co)
            {
                cur_co = nxt_co;
                res ++;
                if (cur_co >= nums.size() - 1) return res;
            }
        }
        return res;
    }
};
// @lc code=end

