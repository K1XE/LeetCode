/*
 * @lc app=leetcode.cn id=743 lang=cpp
 *
 * [743] 网络延迟时间
 */
#include "tools.h"
using namespace std;
// @lc code=start
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<vector<pair<int, int>>> g(n);
        for (auto& e : times)
        {
            int u = e[0] - 1, v = e[1] - 1, w = e[2];
            g[u].emplace_back(v, w);
        }
        using PII = pair<int, int>;
        priority_queue<PII, vector<PII>, greater<PII>> pq;
        vector<int> dis(n, INT_MAX);
        dis[k - 1] = 0;
        pq.emplace(0, k - 1); // dist, node
        while (pq.size())
        {
            auto [d, n] = pq.top();
            pq.pop();
            if (d > dis[n]) continue;
            for (auto& [v, w] : g[n])
            {
                if (dis[v] > dis[n] + w)
                {
                    dis[v] = dis[n] + w;
                    pq.emplace(dis[v], v);
                }
            }
        }
        int res = 0;
        for (auto& d : dis)
        {
            if (d == INT_MAX) return -1;
            res = max(d, res);
        }
        return res;
    }
};
// @lc code=end

