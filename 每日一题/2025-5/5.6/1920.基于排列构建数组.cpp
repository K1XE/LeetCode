/*
 * @lc app=leetcode.cn id=1920 lang=cpp
 *
 * [1920] 基于排列构建数组
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<int> buildArray(vector<int>& nums) {
        vector<int> ans;
        for (auto x : nums)
        {
            ans.push_back(nums[x]);
        }
        return ans;
    }
};
// @lc code=end

