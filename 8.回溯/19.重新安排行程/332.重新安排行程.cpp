/*
 * @lc app=leetcode.cn id=332 lang=cpp
 *
 * [332] 重新安排行程
 */
#include "tools.h"
using namespace std;
// @lc code=start
class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, vector<string>> g;
        for (auto& path : tickets)
        {
            g[path[0]].push_back(path[1]);
        }
        for (auto& path : g)
        {
            string frm = path.first;
            ranges::sort(g[frm], greater<>());
        }
        vector<string> res;
        dfs(res, g, "JFK");
        ranges::reverse(res);
        return res;
    }
    void dfs(vector<string>& res, unordered_map<string, vector<string>>& g, string u)
    {
        while (g[u].size())
        {
            string v = g[u].back();
            g[u].pop_back();
            dfs(res, g, v);
        }
        res.push_back(u);
    }
};
// @lc code=end

