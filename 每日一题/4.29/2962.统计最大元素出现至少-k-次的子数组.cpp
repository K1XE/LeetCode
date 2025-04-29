/*
 * @lc app=leetcode.cn id=2962 lang=cpp
 *
 * [2962] 统计最大元素出现至少 K 次的子数组
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int maxval = 0;
        for (int u = 0; u < nums.size(); u ++ )
        {
            if (nums[u] > maxval) maxval = nums[u];
        }
        int i = 0;
        int cnt = 0;
        long long res = 0;
        for (int j = 0; j < nums.size(); j ++ )
        {
            if (nums[j] == maxval) cnt ++;
            while (cnt >= k)
            {
                res += nums.size() - j;
                if (nums[i] == maxval) cnt --;
                i ++;
            }
        }
        return res;
    }
};
// @lc code=end

