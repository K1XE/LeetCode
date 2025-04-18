/*
 * @lc app=leetcode.cn id=56 lang=cpp
 *
 * [56] 合并区间
 */
#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        ranges::sort(intervals);
        res.emplace_back(intervals[0]);
        for (int i = 1; i < intervals.size(); i ++ )
        {
            if (intervals[i][0] <= res.back()[1])
            {
                res.back()[1] = max(res.back()[1], intervals[i][1]);
            }
            else
            {
                res.emplace_back(intervals[i]);
            }
        }
        return res;
    }
};
// @lc code=end

