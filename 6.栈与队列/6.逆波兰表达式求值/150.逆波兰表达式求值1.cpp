/*
 * @lc app=leetcode.cn id=150 lang=cpp
 *
 * [150] 逆波兰表达式求值
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    stack<int> stk;
    int evalRPN(vector<string>& tokens) {
        
        for (int i = 0; i < tokens.size(); i ++ )
        {
            if (tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" ||tokens[i] == "/")
            {
                int a = stk.top(); stk.pop();
                int b = stk.top(); stk.pop();
                opt(tokens[i], a, b);
            }
            else stk.push(stoi(tokens[i]));
        }
        return stk.top();
    }
private:
    void opt(string o, int a, int b)
    {
        if (o == "+") stk.push(b + a);
        if (o == "-") stk.push(b - a);
        if (o == "*") stk.push(b * a);
        if (o == "/") stk.push(b / a);
    }
};
// @lc code=end

