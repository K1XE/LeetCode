/*
 * @lc app=leetcode.cn id=34 lang=cpp
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 */

// @lc code=start
class Solution {
    public:
        vector<int> searchRange(vector<int>& nums, int target) {
            if (nums.empty()) return {-1, -1};
            int l = 0, r = nums.size() - 1;
            while (l <= r)
            {
                int mid = l + r >> 1;
                if (nums[mid] >= target)
                {
                    r = mid - 1;
                }
                else
                {
                    l = mid + 1;
                }
            }
            if (l >= nums.size() || nums[l] != target) return {-1, -1};
            int left = l;
            l = 0, r = nums.size() - 1;
            while (l <= r)
            {
                int mid = l + r >> 1;
                if (nums[mid] <= target)
                {
                    l = mid + 1;
                }
                else
                {
                    r = mid - 1;
                }
            }
            int right = r;
            return {left, right};
        }
    };
// @lc code=end
