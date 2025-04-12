/*
 * @lc app=leetcode.cn id=34 lang=cpp
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 */

// @lc code=start
class Solution {
    public:
        vector<int> searchRange(vector<int>& nums, int target) {
            int l = 0, r = nums.size() - 1;
            while (l <= r)
            {
                int mid = l + r >> 1;
                if (nums[mid] > target)
                {
                    r = mid - 1;
                }
                else if (nums[mid] < target)
                {
                    l = mid + 1;
                }
                else
                {
                    int s = mid;
                    while (s - 1 >= 0 && nums[s - 1] == target)
                    {
                        s --;
                    }
                    int e = mid;
                    while (e + 1 <= nums.size() - 1 && nums[e + 1] == target)
                    {
                        e ++;
                    }
                    return {s, e};
                }
            }
            return {-1, -1};
        }
    };
// @lc code=end
class Solution {
    public:
        vector<int> searchRange(vector<int>& nums, int target) {
            int l = findleft(nums, target);
            int r = findright(nums, target);
            return {l, r};
        }
    private:
        int findleft(vector<int>& nums, int target)
        {
            int lb = -1, l = 0, r = nums.size() - 1;
            while (l <= r)
            {
                int mid = l + r >> 1;
                if (nums[mid] >= target)
                {
                    r = mid - 1;
                    if (nums[mid] == target) lb = mid;
                }
                else
                {
                    l = mid + 1;
                }
            }
            return lb;
        }
        int findright(vector<int>& nums, int target)
        {
            int rb = -1, l = 0, r = nums.size() - 1;
            while (l <= r)
            {
                int mid = l + r >> 1;
                if (nums[mid] > target)
                {
                    r = mid - 1;
                }
                else
                {
                    l = mid + 1;
                    if (nums[mid] == target) rb = mid;
                }
            }
            return rb;
        }
    };
