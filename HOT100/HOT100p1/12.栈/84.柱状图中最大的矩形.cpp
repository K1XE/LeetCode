/*
 * @lc app=leetcode.cn id=84 lang=cpp
 *
 * [84] 柱状图中最大的矩形
 */
#include "tools.h"
// @lc code=start
class Solution
{
public:
    int largestRectangleArea(vector<int> &heights)
    {
        heights.push_back(-1);
        int n = heights.size();
        int res = 0;
        stack<int> stk;
        stk.push(-1);
        for (int right = 0; right < n; right++)
        {
            while (stk.size() > 1 && heights[right] <= heights[stk.top()])
            {
                int i = stk.top();
                stk.pop();
                int left = stk.top();
                res = max(res, (right - 1 - (left + 1) + 1) * heights[i]);
            }
            stk.push(right);
        }
        return res;
    }
};
// @lc code=end

class Solution
{
public:
    int largestRectangleArea(vector<int> &heights)
    {
        int n = heights.size();
        vector<int> left(n, -1);
        vector<int> right(n, n);
        stack<int> stk;
        for (int i = 0; i < n; i++)
        {
            while (stk.size() && heights[i] <= heights[stk.top()])
            {
                right[stk.top()] = i;
                stk.pop();
            }
            if (stk.size())
                left[i] = stk.top();
            stk.push(i);
        }

        int res = 0;
        for (int i = 0; i < n; i++)
        {
            res = max(res, (right[i] - 1 - (left[i] + 1) + 1) * heights[i]);
        }
        return res;
    }
};

class Solution
{
public:
    int largestRectangleArea(vector<int> &heights)
    {
        int n = heights.size();
        vector<int> left(n, -1);
        stack<int> stk;
        for (int i = 0; i < n; i++)
        {
            while (stk.size() && heights[i] <= heights[stk.top()])
            {
                stk.pop();
            }
            if (stk.size())
                left[i] = stk.top();
            stk.push(i);
        }
        vector<int> right(n, n);
        stk = stack<int>();
        for (int i = n - 1; i >= 0; i--)
        {
            while (stk.size() && heights[i] <= heights[stk.top()])
            {
                stk.pop();
            }
            if (stk.size())
                right[i] = stk.top();
            stk.push(i);
        }
        int res = 0;
        for (int i = 0; i < n; i++)
        {
            res = max(res, (right[i] - 1 - (left[i] + 1) + 1) * heights[i]);
        }
        return res;
    }
};