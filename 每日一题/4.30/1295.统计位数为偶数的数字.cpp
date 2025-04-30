/*
 * @lc app=leetcode.cn id=1295 lang=cpp
 *
 * [1295] 统计位数为偶数的数字
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int res = 0;
        for (auto x : nums)
        {
            if (! (solve(x) % 2)) res ++;
        }
        return res;
    }
    int solve(int num)
    {
        int res = 0;
        while (num)
        {
            res += 1;
            num /= 10;
        }
        return res;
    }
};
// @lc code=end

