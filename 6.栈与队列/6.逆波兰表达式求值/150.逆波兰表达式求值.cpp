/*
 * @lc app=leetcode.cn id=150 lang=cpp
 *
 * [150] 逆波兰表达式求值
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;
        int res = 0;
        for (auto s : tokens)
        {
            if (s != "+" && s != "-" && s != "*" && s != "/")
            {
                stk.push(stoi(s));
            }
            else
            {
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                int tmp = 0;
                if (s == "+") tmp = b + a;
                else if (s == "-") tmp = b - a;
                else if (s == "*") tmp = b * a;
                else tmp = b / a;
                stk.push(tmp);
            }
        }
        return stk.top();
    }
};
// @lc code=end

