/*
 * @lc app=leetcode.cn id=53 lang=cpp
 *
 * [53] 最大子数组和
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int prefix = 0;
        int minP = 0;
        int res = INT32_MIN;
        for (int i = 0; i < nums.size(); i ++ )
        {
            prefix += nums[i];
            minP = min(minP, prefix);
            res = max(res, prefix - minP);
        }
        return res;
    }
};
// @lc code=end
class Solution {
    public:
        int maxSubArray(vector<int>& nums) {
            int sums = 0;
            int maxSum = INT32_MIN;
            for (int i = 0; i < nums.size(); i ++ )
            {
                sums += nums[i];
                maxSum = max(maxSum, sums);
                if (sums < 0) sums = 0;
            }
            return maxSum;
        }
    };
