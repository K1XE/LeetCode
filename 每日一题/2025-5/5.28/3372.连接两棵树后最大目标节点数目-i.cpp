/*
 * @lc app=leetcode.cn id=3372 lang=cpp
 *
 * [3372] 连接两棵树后最大目标节点数目 I
 */
#include "tools.h"
// @lc code=start
class Solution {
public:

    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2, int k) {
        auto build = [&] (vector<vector<int>>& edges)
        {
            vector<vector<int>> g(edges.size() + 1);
            for (auto& e : edges)
            {
                int u = e[0], v = e[1];
                g[u].push_back(v);
                g[v].push_back(u);
            }
            return g;
        };
        auto dfs = [&] (auto&& self, int d, int k, int fa, int cur, vector<vector<int>>& g)
        {
            if (d > k) return 0;
            int cnt = 1;
            for (auto& u : g[cur])
            {
                if (u != fa)
                {
                    cnt += self(self, d + 1, k, cur, u, g);
                }
            }
            return cnt;
        };
        int max2 = 0;
        if (k > 0)
        {
            auto tree2 = build(edges2);
            for (int i = 0; i < edges2.size() + 1; i ++ )
            {
                max2 = max(max2, dfs(dfs, 0, k - 1, -1, i, tree2));
            }
        }
        auto tree1 = build(edges1);
        vector<int> res(edges1.size() + 1);
        for (int i = 0; i < res.size(); i ++ )
        {
            res[i] = dfs(dfs, 0, k, -1, i, tree1) + max2;
        }
        return res;
    }
};
// @lc code=end

