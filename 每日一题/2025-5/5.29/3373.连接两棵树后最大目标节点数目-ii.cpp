/*
 * @lc app=leetcode.cn id=3373 lang=cpp
 *
 * [3373] 连接两棵树后最大目标节点数目 II
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        auto res2 = this->countf(edges2);
        auto cnt2 = res2.second;
        auto max2 = max(cnt2[0], cnt2[1]);
        auto res1 = this->countf(edges1);
        auto g = res1.first;
        auto cnt1 = res1.second;
        vector<int> res(g.size(), max2);
        auto dfs = [&](auto&& self, int cur, int fa, int d) -> void
        {
            res[cur] += cnt1[d];
            for (auto v : g[cur])
            {
                if (v != fa)
                {
                    self(self, v, cur, d ^ 1);
                }
            }
        };
        dfs(dfs, 0, -1, 0);
        return res;
    }
private:
    pair<vector<vector<int>>, vector<int>> countf(vector<vector<int>>& edges)
    {
        int sz = edges.size() + 1;
        vector<vector<int>> g(sz);
        for (auto& e : edges)
        {
            int u = e[0], v = e[1];
            g[u].push_back(v);
            g[v].push_back(u);
        }
        vector<int> cnt = {0, 0};
        auto dfs = [&](auto&& self, int cur, int fa, int d) -> void
        {
            cnt[d] += 1;
            for (auto v : g[cur])
            {
                if (v != fa)
                {
                    self(self, v, cur, d ^ 1);
                }
            }
        };
        dfs(dfs, 0, -1, 0);
        return {g, cnt};
    }
};
// @lc code=end

