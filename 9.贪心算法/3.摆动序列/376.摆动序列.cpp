/*
 * @lc app=leetcode.cn id=376 lang=cpp
 *
 * [376] 摆动序列
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    int dp[1005][2];
    int wiggleMaxLength(vector<int>& nums) {
        memset(dp, 0, sizeof(dp));
        dp[0][0] = dp[0][1] = 1;
        for (int i = 1; i < nums.size(); i ++ )
        {
            dp[i][0] = dp[i][1] = 1;
            for (int j = 0; j < i; j ++ )
            {
                if (nums[j] > nums[i])
                {
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1);
                }
            }
            for (int j = 0; j < i; j ++ )
            {
                if (nums[j] < nums[i])
                {
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1);
                }
            }
        }
        return max(dp[nums.size() - 1][1], dp[nums.size() - 1][0]);
    }
};
// @lc code=end

class Solution {
    public:
        int wiggleMaxLength(vector<int>& nums) {
            int lastdiff = 0;
            int res = 1;
            for (int i = 1; i < nums.size(); i ++ )
            {
                int curdiff = nums[i] - nums[i - 1];
                if ((lastdiff >= 0 && curdiff < 0) || (lastdiff <= 0 && curdiff > 0))
                {
                    res ++;
                    lastdiff = curdiff;
                }
                else if (curdiff != 0) lastdiff = curdiff;
            }
            return res;
        }
    };