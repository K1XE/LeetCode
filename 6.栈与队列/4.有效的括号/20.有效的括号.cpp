/*
 * @lc app=leetcode.cn id=20 lang=cpp
 *
 * [20] 有效的括号
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    bool isValid(string s) {
        if (s.size() % 2) return 0;
        stack<char> stk;
        for (int i = 0; i < s.size(); i ++ )
        {
            if (s[i] == '(') stk.push(')');
            else if (s[i] == '[') stk.push(']');
            else if (s[i] == '{') stk.push('}');
            else if (stk.empty() || stk.top() != s[i]) return 0;
            else stk.pop();
        }
        return stk.empty();
    }
};
// @lc code=end
class Solution {
    public:
        bool isValid(string s) {
            if (s.size() % 2) return 0;
            stack<char> stk;
            int step = 0;
            while (step < s.size())
            {
                if (s[step] == '(' || s[step] == '[' || s[step] == '{')
                {
                    stk.push(s[step ++]);
                }
                else
                {
                    if (stk.empty()) return 0;
                    if ((s[step] == ')' && stk.top() == '(') || (s[step] == ']' && stk.top() == '[') || (s[step] == '}' && stk.top() == '{'))
                    {
                        stk.pop();
                        step ++;
                    }
                    else return 0;
                }
            }
            return stk.empty();
        }
    };
