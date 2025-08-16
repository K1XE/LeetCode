/*
 * @lc app=leetcode.cn id=283 lang=cpp
 *
 * [283] 移动零
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0;
        for (; i < nums.size(); i ++)
        {
            if (nums[i] == 0) break;
        }
        int j = i + 1;
        while (j < nums.size())
        {
            if (nums[i] != 0) i ++;
            else if (nums[j] == 0) j ++;
            else if (nums[i] == 0 && nums[j] != 0) swap(nums[i ++], nums[j ++]);
        }
    }
};
// @lc code=end

