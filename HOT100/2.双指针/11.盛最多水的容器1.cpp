/*
 * @lc app=leetcode.cn id=11 lang=cpp
 *
 * [11] 盛最多水的容器
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() - 1;
        int res = 0;
        while (l <= r)
        {
            res = max(res, min(height[l], height[r]) * (r - l));
            if (height[l] < height[r]) l ++;
            else r --;
        }
        return res;
    }
};
// @lc code=end

