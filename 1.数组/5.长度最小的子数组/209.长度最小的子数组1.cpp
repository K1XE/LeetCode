/*
 * @lc app=leetcode.cn id=209 lang=cpp
 *
 * [209] 长度最小的子数组
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int i = 0;
        int minLen = INT_MAX;
        int sums = 0;
        for (int j = 0; j < nums.size(); j ++ )
        {
            sums += nums[j];
            while (sums >= target)
            {
                int len = j - i + 1;
                minLen = min(minLen, len);
                sums -= nums[i ++];
            }
        }
        return minLen == INT_MAX ? 0 : minLen;
    }
};
// @lc code=end

