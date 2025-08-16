/*
 * @lc app=leetcode.cn id=84 lang=cpp
 *
 * [84] 柱状图中最大的矩形
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(-1);
        int n = heights.size();
        int res = 0;
        stack<int> stk;
        stk.push(-1);
        for (int r = 0; r < n; r ++ )
        {
            while (stk.size() > 1 && heights[r] <= heights[stk.top()])
            {
                int i = stk.top();
                stk.pop();
                int l = stk.top();
                res = max(res, (r - l - 1) * heights[i]);
            }
            stk.push(r);
        }
        return res;
    }
};
// @lc code=end

class Solution {
    public:
        int largestRectangleArea(vector<int>& heights) {
            int n = heights.size();
            vector<int> left(n, -1);
            vector<int> right(n, n);
            stack<int> stk;
            for (int i = 0; i < n; i ++ )
            {
                while (stk.size() && heights[i] <= heights[stk.top()])
                {
                    stk.pop();
                }
                if (stk.size()) left[i] = stk.top();
                stk.push(i);
            }
            stk = stack<int>();
            for (int i = n - 1; i >= 0; i -- )
            {
                while (stk.size() && heights[i] <= heights[stk.top()])
                {
                    stk.pop();
                }
                if (stk.size()) right[i] = stk.top();
                stk.push(i);
            }
            int res = 0;
            for (int i = 0; i < n; i ++ )
            {
                res = max(res, heights[i] * (right[i] - left[i] - 1));
            }
            
            return res;
        }
    };