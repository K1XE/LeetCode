/*
 * @lc app=leetcode.cn id=977 lang=cpp
 *
 * [977] 有序数组的平方
 */

// @lc code=start
class Solution {
    public:
        vector<int> sortedSquares(vector<int>& nums) {
            vector<int> backup(nums.size(), 0);
            
            int l = 0, r = nums.size() - 1, cnt = nums.size() - 1;
            while (l <= r)
            {
                int ln = nums[l] * nums[l], rn = nums[r] * nums[r];
                if (ln > rn)
                {
                    backup[cnt --] = ln, l ++;
                }
                else
                {
                    backup[cnt --] = rn, r --;
                }
            }
            return backup;
        }
    };
// @lc code=end
