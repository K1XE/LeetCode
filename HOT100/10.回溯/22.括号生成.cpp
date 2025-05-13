/*
 * @lc app=leetcode.cn id=22 lang=cpp
 *
 * [22] 括号生成
 */
#include "tools.h"
// @lc code=start
class Solution
{
public:
    vector<string> generateParenthesis(int n)
    {
        int _n = n * 2;
        vector<string> res;
        string pack = "(";
        int cnt1 = 1, cnt2 = 0;
        auto dfs = [&](auto &&self) -> void
        {
            if (pack.size() == _n)
            {
                res.emplace_back(pack);
                return;
            }
            if (cnt1 < n)
            {
                cnt1++;
                pack += "(";
                self(self);
                pack.pop_back();
                cnt1--;
            }
            if (cnt2 < cnt1)
            {
                cnt2++;
                pack += ")";
                self(self);
                pack.pop_back();
                cnt2--;
            }
        };
        dfs(dfs);
        return res;
    }
};
// @lc code=end

class Solution
{
public:
    vector<string> generateParenthesis(int n)
    {
        int _n = n * 2;
        vector<string> res;
        string pack = "(";
        int cnt1 = 1, cnt2 = 0;
        unordered_set<string> ss;
        auto check = [&](string &pack) -> bool
        {
            stack<char> stk;
            for (int i = 0; i < pack.size(); i++)
            {
                if (pack[i] == ')')
                {
                    if (stk.size() && stk.top() == '(')
                    {
                        stk.pop();
                        continue;
                    }
                    else
                        return 0;
                }
                else
                    stk.push(pack[i]);
            }
            return stk.empty();
        };
        auto dfs = [&](auto &&self) -> void
        {
            if (pack.size() == _n)
            {
                if (check(pack) && !ss.contains(pack))
                {
                    ss.insert(pack);
                    res.emplace_back(pack);
                }
                return;
            }
            if (cnt1 < n)
            {
                cnt1++;
                pack += "(";
                self(self);
                pack.pop_back();
                cnt1--;
            }
            if (cnt2 < n)
            {
                cnt2++;
                pack += ")";
                self(self);
                pack.pop_back();
                cnt2--;
            }
        };
        dfs(dfs);
        return res;
    }
};