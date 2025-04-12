/*
 * @lc app=leetcode.cn id=704 lang=cpp
 *
 * [704] 二分查找
 */

// @lc code=start
class Solution {
    public:
        int search(vector<int>& nums, int target) {
            int l = 0, r = nums.size() - 1;
            
            while (l <= r)
            {
                int mid_pos = l + r >> 1;
                int mid = nums[mid_pos];
                if (mid > target)
                {
                    r = mid_pos - 1;
                }
                else if (mid < target)
                {
                    l = mid_pos + 1;
                }
                else
                {
                    return mid_pos;
                }
            }
            return -1;
    
        }
    };
// @lc code=end

