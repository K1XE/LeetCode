/*
 * @lc app=leetcode.cn id=452 lang=cpp
 *
 * [452] 用最少数量的箭引爆气球
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    static bool cmp(vector<int>& a, vector<int>& b)
    {
        return a[0] < b[0];
    }
    int findMinArrowShots(vector<vector<int>>& points) {
        ranges::sort(points, cmp);
        int res = 1;
        int n = points.size();
        for (int i = 1; i < n; i ++ )
        {
            if (points[i][0] > points[i - 1][1]) res ++;
            else points[i][1] = min(points[i][1], points[i - 1][1]);
        }
        return res;
    }
};
// @lc code=end

