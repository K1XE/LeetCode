/*
 * @lc app=leetcode.cn id=209 lang=cpp
 *
 * [209] 长度最小的子数组
 */

// @lc code=start
class Solution {
    public:
        int minSubArrayLen(int target, vector<int>& nums) {
            int i = 0, sums = 0;
            int minLen = INT32_MAX, len = INT32_MAX;
            for (int j = 0; j < nums.size(); j ++ )
            {
                
                sums += nums[j];
                while (sums >= target)
                {
                    len = j - i + 1;
                    minLen = min(minLen, len);
                    sums -= nums[i];
                    i ++;
                }
            }
            return minLen == INT32_MAX ? 0 : minLen;
        }
    };
// @lc code=end

