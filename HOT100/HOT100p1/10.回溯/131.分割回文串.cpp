/*
 * @lc app=leetcode.cn id=131 lang=cpp
 *
 * [131] 分割回文串
 */
#include "tools.h"

// @lc code=start
class Solution {
public:
    vector<vector<string>> partition(string s) {
        
        vector<vector<string>> res;
        vector<string> pack;
        int n = s.size();

        auto check = [&](string sub) -> bool
        {
            int l = 0, r = sub.size() - 1;
            while (l <= r)
            {
                if (sub[l] != sub[r]) return 0;
                l ++, r --;
            }
            return 1;
        };

        auto dfs = [&](auto&& self, int sta) -> void
        {
            if (sta == n)
            {
                res.emplace_back(pack);
                return;
            }
            for (int i = sta; i < n; i ++ )
            {
                string sub = s.substr(sta, i - sta + 1);
                if (!check(sub)) continue;
                pack.push_back(sub);
                self(self, i + 1);
                pack.pop_back();
            }
        };

        dfs(dfs, 0);
        return res;
    }
};
// @lc code=end

