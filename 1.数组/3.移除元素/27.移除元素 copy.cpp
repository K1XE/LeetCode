/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */

// @lc code=start
class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            int l = 0, r = nums.size() - 1, cnt = 0;
            while (l <= r)
            {
                if (nums[l] == val && nums[r] == val)
                {
                    cnt ++, r --;
                }
                else if (nums[l] == val && nums[r] != val)
                {
                    swap(nums[l], nums[r]);
                    cnt ++, l ++, r --;
                }
                else
                {
                    l ++;
                }
            }
            return nums.size() - cnt;
        }
    };
// @lc code=end
