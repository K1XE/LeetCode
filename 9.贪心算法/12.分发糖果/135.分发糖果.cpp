/*
 * @lc app=leetcode.cn id=135 lang=cpp
 *
 * [135] 分发糖果
 */
#include "tools.h"
// @lc code=start
class Solution
{
public:
    int candy(vector<int> &ratings)
    {
        int n = ratings.size();

        vector<int> l(n, 1);
        vector<int> r(n, 1);
        for (int i = 1; i < n; i++)
        {
            if (ratings[i] > ratings[i - 1])
                l[i] = l[i - 1] + 1;
        }
        for (int i = n - 2; i >= 0; i--)
        {
            if (ratings[i] > ratings[i + 1])
                r[i] = r[i + 1] + 1;
        }
        int sums = 0;
        for (int i = 0; i < n; i ++)
        {
            sums += max(l[i], r[i]);
        }
        return sums;
    }
};
// @lc code=end
