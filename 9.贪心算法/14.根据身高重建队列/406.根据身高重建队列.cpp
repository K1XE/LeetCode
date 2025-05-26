/*
 * @lc app=leetcode.cn id=406 lang=cpp
 *
 * [406] 根据身高重建队列
 */
#include "tools.h"
// @lc code=start
class Solution
{
public:
    static bool cmp(vector<int> &a, vector<int> &b)
    {
        if (a[0] == b[0])
            return a[1] < b[1];
        return a[0] > b[0];
    }
    vector<vector<int>> reconstructQueue(vector<vector<int>> &people)
    {
        ranges::sort(people, cmp);
        list<vector<int>> res;
        for (auto p : people)
        {
            int pos = p[1];
            auto it = res.begin();
            while (pos --)
            {
                it ++;
            }
            res.insert(it, p);
        }
        return vector<vector<int>>(res.begin(), res.end());
    }
};
// @lc code=end
