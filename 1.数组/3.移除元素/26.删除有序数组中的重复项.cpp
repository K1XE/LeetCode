/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
class Solution {
    public:
        int removeDuplicates(vector<int>& nums) {
            int l1 = 0, l2 = 1, f = 0;
            while (l2 < nums.size())
            {
                if (nums[l1] != nums[l2])
                {
                    nums[++ l1] = nums[l2];
                }
                l2 ++;
            }
            return l1 + 1;
        }
    };
// @lc code=end

class Solution {
    public:
        int removeDuplicates(vector<int>& nums) {
            int l1 = 0, l2 = 1, f = 0;
            nums[f ++] = nums[l1];
            while (l2 < nums.size())
            {
                while (l2 < nums.size() && nums[l1] == nums[l2])
                {
                    l1 ++, l2 ++;
                }
                if (l2 >= nums.size()) break;
                nums[f ++] = nums[l2];
                l1 ++, l2 ++;
            }
            return f;
        }
    };