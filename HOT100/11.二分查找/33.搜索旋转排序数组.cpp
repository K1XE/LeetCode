/*
 * @lc app=leetcode.cn id=33 lang=cpp
 *
 * [33] 搜索旋转排序数组
 */
#include "tools.h"
using namespace std;
// @lc code=start
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r)
        {
            int mid = l + r >> 1;
            if (nums[mid] == target) return mid;
            if (nums[l] <= nums[mid])
            {
                if (nums[l] <= target && target < nums[mid]) r = mid - 1;
                else l = mid + 1;
            }
            else
            {
                if (nums[mid] < target && target <= nums[r]) l = mid + 1;
                else r = mid - 1;
            }
        }
        return -1;
    }
};
// @lc code=end

