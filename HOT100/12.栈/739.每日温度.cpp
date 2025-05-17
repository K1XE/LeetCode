/*
 * @lc app=leetcode.cn id=739 lang=cpp
 *
 * [739] 每日温度
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<int> stk;
        int n = temperatures.size();
        vector<int> res(n, 0);
        for (int i = 0; i < n; i ++ )
        {
            while (stk.size() && temperatures[i] > temperatures[stk.top()])
            {
                int pre = stk.top();
                stk.pop();
                res[pre] = i - pre;
            }
            stk.push(i);
        }
        return res;
    }
};
// @lc code=end

