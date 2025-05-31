/*
 * @lc app=leetcode.cn id=2302 lang=cpp
 *
 * [2302] 统计得分小于 K 的子数组数目
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    long long countSubarrays(vector<int>& nums, long long k) {
        long long res = 0;
        long long sums = 0;
        int i = 0;
        for (int j = 0; j < nums.size(); j ++ )
        {
            sums += nums[j];
            while (sums * (j - i + 1) >= k)
            {
                sums -= nums[i ++];
            }
            res += j - i + 1;
        }
        return res;
    }
};
// @lc code=end

