/*
 * @lc app=leetcode.cn id=41 lang=cpp
 *
 * [41] 缺失的第一个正数
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        for (auto& x : nums)
        {
            if (x <= 0) x = n + 1;
        }
        for (auto x : nums)
        {
            int a = abs(x);
            if (a <= n)
            {
                nums[a - 1] = -abs(nums[a - 1]);
            }
        }
        for (int i = 0; i < n; i ++ )
        {
            if (nums[i] > 0) return i + 1;
        }
        return n + 1;
    }
};
// @lc code=end

class Solution {
    public:
        int firstMissingPositive(vector<int>& nums) {
            for (int i = 0; i < nums.size(); i ++ )
            {
                while (nums[i] >= 1 && nums[i] < nums.size() && nums[i] != nums[nums[i] - 1])
                {
                    int j = nums[i] - 1;
                    swap(nums[i], nums[j]);
                }
            }
            for (int i = 0; i < nums.size(); i ++ )
            {
                if (nums[i] != i + 1) return i + 1;
            }
            return nums.size() + 1;
        }
    };