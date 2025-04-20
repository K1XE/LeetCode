/*
 * @lc app=leetcode.cn id=20 lang=cpp
 *
 * [20] 有效的括号
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;
        for (int i = 0; i < s.size(); i ++ )
        {
            if (s[i] == '(') stk.push(')');
            else if (s[i] == '[') stk.push(']');
            else if (s[i] == '{') stk.push('}');
            else
            {
                if (stk.empty() || s[i] != stk.top()) return 0;
                stk.pop();
            }
        }
        return stk.empty();
    }
};
// @lc code=end

