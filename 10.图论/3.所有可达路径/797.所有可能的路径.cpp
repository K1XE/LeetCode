/*
 * @lc app=leetcode.cn id=797 lang=cpp
 *
 * [797] 所有可能的路径
 */
#include "tools.h"
// @lc code=start
class Solution {
public:
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        vector<vector<int>> res;
        vector<int> path;
        int n = graph.size();
        auto dfs = [&] (auto&& self, int u, int n) -> void
        {
            if (u == n - 1)
            {
                res.emplace_back(path);
                return;
            }
            for (auto& v : graph[u])
            {
                path.push_back(v);
                self(self, v, n);
                path.pop_back();
            }
        };
        path.push_back(0);
        dfs(dfs, 0, n);
        return res;
    }
};
// @lc code=end

class Solution {
    public:
        vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
            vector<vector<int>> res;
            vector<int> path;
            int n = graph.size();
            auto dfs = [&] (auto&& self, int u, int n) -> void
            {
                path.push_back(u);
                if (u == n - 1)
                {
                    res.emplace_back(path);
                }
                else
                {
                    for (auto& v : graph[u])
                    {
                        self(self, v, n);
                    }
                }
                path.pop_back();
            };
            dfs(dfs, 0, n);
            return res;
        }
    };