/*
 * @lc app=leetcode.cn id=283 lang=cpp
 *
 * [283] 移动零
 */

// @lc code=start
class Solution {
    public:
        void moveZeroes(vector<int>& nums) {
            if (nums.size() == 1) return;
            for (int i = 0, j = 1; i < nums.size() && j < nums.size();)
            {
                if (nums[i] == 0 && nums[j] != 0)
                {
                    swap(nums[i], nums[j]);
                }
                else if (nums[i] == 0 && nums[j] == 0)
                {
                    j ++;
                }
                else if (nums[i] != 0 && nums[j] == 0)
                {
                    i ++;
                }
                else
                {
                    i ++, j ++;
                }
            }
            return;
        }
    };
// @lc code=end
class Solution {
    public:
        void moveZeroes(vector<int>& nums) {
            int i = 0, j = 0;
            while (j < nums.size())
            {
                if (nums[j])
                {
                    swap(nums[i], nums[j]);
                    i ++;
                }
                j ++;
            }
        }
    };
