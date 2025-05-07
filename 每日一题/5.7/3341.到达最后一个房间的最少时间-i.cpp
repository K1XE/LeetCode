/*
 * @lc app=leetcode.cn id=3341 lang=cpp
 *
 * [3341] 到达最后一个房间的最少时间 I
 */
#include "tools.h"
using namespace std;
// @lc code=start
class Solution {
public:
    vector<vector<int>> d = {{0, 1}, {0, -1}, {1, 0}, {-1 ,0}};
    int minTimeToReach(vector<vector<int>>& g) {
        int n = g.size(), m = g[0].size();
        vector<vector<int>> dis(n, vector<int>(m, INT_MAX));
        dis[0][0] = 0;
        using pack = vector<int>;
        priority_queue<pack, vector<pack>, greater<pack>> heap;
        heap.push({0, 0, 0});
        while (heap.size())
        {
            auto tmp = heap.top();
            int i = tmp[1], j = tmp[2], w = tmp[0];
            heap.pop();
            if (i == n - 1 && j == m - 1) return w;
            if (w > dis[i][j]) continue;
            for (auto& tmp : d)
            {
                int dx = tmp[0];
                int dy = tmp[1];
                int ni = i + dx, nj = j + dy;
                if (ni >= 0 && ni < n && nj >= 0 && nj < m)
                {
                    int nxt_time = max(w, g[ni][nj]) + 1;
                    if (nxt_time < dis[ni][nj])
                    {
                        dis[ni][nj] = nxt_time;
                        heap.emplace(vector<int>{nxt_time, ni, nj});
                    }
                }
            }
        }
        return -1;
    }
};
// @lc code=end

