/*
 * @lc app=leetcode.cn id=71 lang=cpp
 *
 * [71] 简化路径
 */
#include <bits/stdc++.h>
#include <ranges>
using namespace std;
// @lc code=start
class Solution {
public:
    string simplifyPath(string path) {
        int i = 0;
        stack<string> stk;
        while (i < path.size())
        {
            if (path[i] == '/') i ++;
            string s;
            while (i < path.size() && path[i] != '/') s += path[i ++];
            if (s == "..")
            {
                if (stk.size()) stk.pop();
                continue;
            }
            if (s != "." && s.size()) stk.push(s);
        }
        string res;
        while (stk.size())
        {
            ranges::reverse(stk.top());
            res += stk.top();
            stk.pop();
            res += "/";
        }
        ranges::reverse(res);
        return res.size() ? res : "/";
    }
};
// @lc code=end

