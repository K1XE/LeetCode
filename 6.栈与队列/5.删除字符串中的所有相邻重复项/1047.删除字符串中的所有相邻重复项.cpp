/*
 * @lc app=leetcode.cn id=1047 lang=cpp
 *
 * [1047] 删除字符串中的所有相邻重复项
 */
#include <bits/stdc++.h>
using namespace std;
// @lc code=start
class Solution {
public:
    string removeDuplicates(string s) {
        string res;
        for (auto c : s)
        {
            if (res.empty() || res.back() != c) res += c;
            else res.pop_back();
        }
        return res;
    }
};
// @lc code=end
class Solution {
    public:
        string removeDuplicates(string s) {
            stack<char> stk;
            for (auto c : s)
            {
                if (stk.empty() || c != stk.top())
                {
                    stk.push(c);
                }
                else
                {
                    stk.pop();
                }
            }
            string res;
            while (stk.size())
            {
                res += stk.top();
                stk.pop();
            }
            reverse(res.begin(), res.end());
            return res;
        }
    };
