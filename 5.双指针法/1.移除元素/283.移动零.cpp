/*
 * @lc app=leetcode.cn id=283 lang=cpp
 *
 * [283] 移动零
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0, j = 1;
        while (j < nums.size())
        {
            if (nums[i] == 0 && nums[j] != 0)
            {
                swap(nums[i ++], nums[j ++]);
            }
            else if (nums[i] == 0 && nums[j] == 0)
            {
                j ++;
            }
            else if (nums[i] != 0 && nums[j] == 0)
            {
                i ++, j ++;
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

