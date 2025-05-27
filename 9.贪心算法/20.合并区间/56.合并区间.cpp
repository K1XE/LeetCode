/*
 * @lc app=leetcode.cn id=56 lang=cpp
 *
 * [56] 合并区间
 */
#include "tools.h"
// @lc code=start
class Solution
{
public:
    static bool cmp(vector<int> &a, vector<int> &b)
    {
        if (a[0] != b[0]) return a[0] < b[0];
        else return a[1] < b[1];
    }
    vector<vector<int>> merge(vector<vector<int>> &_in)
    {
        ranges::sort(_in, cmp);
        int n = _in.size();
        int ends = _in[0][1];
        int starts = _in[0][0];
        vector<vector<int>> res;
        for (int i = 1; i < n; i ++ )
        {
            if (ends < _in[i][0])
            {
                res.push_back(vector<int>{starts, ends});
                ends = _in[i][1];
                starts = _in[i][0];
            }
            else
            {
                ends = max(ends, _in[i][1]);
            }
        }
        res.push_back(vector<int>{starts, ends});
        return res;
    }
};
// @lc code=end
