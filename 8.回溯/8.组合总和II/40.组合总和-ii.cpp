/*
 * @lc app=leetcode.cn id=40 lang=cpp
 *
 * [40] 组合总和 II
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& c, int t) {
        ranges::sort(c);
        vector<vector<int>> res;
        vector<int> pack;
        vector<bool> vis(c.size(), 0);
        dfs(0, t, res, pack, 0, c, vis);
        return res;
    }
    void dfs(int sums, int t, vector<vector<int>>& res, vector<int>& pack, int sta, vector<int>& c, vector<bool>& vis)
    {
        if (sums == t)
        {
            res.emplace_back(pack);
            return;
        }
        for (int i = sta; i < c.size(); i ++ )
        {
            if (i > sta && c[i] == c[i - 1] && vis[i] == 0) continue;
            sums += c[i];
            vis[i] = 1;
            if (sums > t)
            {
                sums -= c[i];
                break;
            }
            pack.push_back(c[i]);
            dfs(sums, t, res, pack, i + 1, c, vis);
            pack.pop_back();
            vis[i] = 0;
            sums -= c[i];
        }
    }
};
// @lc code=end

