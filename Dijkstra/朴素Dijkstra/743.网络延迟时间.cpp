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
        vector<vector<int>> g(n, vector<int>(n, INT_MAX));
        for (auto& pack : times)
        {
            int x = pack[0], y = pack[1], w = pack[2];
            g[x - 1][y - 1] = w;
        }
        vector<int> dis(n, INT_MAX);
        vector<bool> done(n, 0);
        dis[k - 1] = 0;
        int res = dis[k - 1];
        while (1)
        {
            int x = -1;
            for (int i = 0; i < n; i ++ )
            {
                if (! done[i] && (x < 0 || dis[x] > dis[i]))
                {
                    x = i;
                }
            }
            if (x < 0)
            {
                return res;
            }
            if (dis[x] == INT_MAX) return -1;
            res = dis[x];
            done[x] = 1;
            for (int i = 0; i < n; i ++ )
            {
                if (g[x][i] != INT_MAX)
                    dis[i] = min(dis[i], g[x][i] + dis[x]);
            }
        }
    }
};
// @lc code=end

