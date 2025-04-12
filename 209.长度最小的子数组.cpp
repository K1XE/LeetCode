/*
 * @lc app=leetcode.cn id=209 lang=cpp
 *
 * [209] 长度最小的子数组
 */

// @lc code=start
class Solution {
    public:
        int minSubArrayLen(int target, vector<int>& nums) {
            int res = INT32_MAX;
            int sums = 0;
            int i = 0;
            for (int j = 0; j < nums.size(); j ++ )
            {
                sums += nums[j];
                while (sums >= target)
                {
                    int len = j - i + 1;
                    res = len < res ? len : res;
                    sums -= nums[i ++ ];
                }
            }
            return res == INT32_MAX ? 0 : res;
        }
    };
// @lc code=end

