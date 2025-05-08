/*
 * @lc app=leetcode.cn id=131 lang=cpp
 *
 * [131] 分割回文串
 */
#include "tools.h"
using namespace std;
// @lc code=start
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> pack;
        dfs(s, 0, s.size(), res, pack);
        return res;
    }
    bool check(string& s)
    {
        int l = 0, r = s.size() - 1;
        while (l <= r)
        {
            if (s[l] != s[r]) return 0;
            l ++, r --;
        }
        return 1;
    }
    void dfs(string& s, int sta, int n, vector<vector<string>>& res, vector<string>& pack)
    {
        if (sta >= n)
        {
            res.emplace_back(pack);
            return;
        }
        for (int i = sta; i < n; i ++ )
        {
            string sub = s.substr(sta, i - sta + 1);
            if (! check(sub)) continue;
            pack.emplace_back(sub);
            dfs(s, i + 1, n, res, pack);
            pack.pop_back();
        }
    }
};
// @lc code=end

