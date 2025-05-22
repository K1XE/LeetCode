/*
 * @lc app=leetcode.cn id=376 lang=cpp
 *
 * [376] 摆动序列
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int post_diff = 0;
        int res = 1;
        int cur_diff = 0;
        int n = nums.size();
        for (int i = 1; i < n; i ++ )
        {
            cur_diff = nums[i] - nums[i - 1];
            if ((post_diff >= 0 && cur_diff < 0) || (post_diff <= 0 && cur_diff > 0))
            {
                post_diff = cur_diff;
                res ++;
            }
            else if (cur_diff != 0) post_diff = cur_diff;
        }
        return res;
    }
};
// @lc code=end

