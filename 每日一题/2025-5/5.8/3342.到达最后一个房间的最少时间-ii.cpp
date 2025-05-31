/*
 * @lc app=leetcode.cn id=3342 lang=cpp
 *
 * [3342] 到达最后一个房间的最少时间 II
 */
#include "tools.h"
using namespace std;
// @lc code=start
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int m = moveTime.size(), n = moveTime[0].size();
        vector<vector<int>> dis(m, vector<int>(n, INT_MAX));
        dis[0][0] = 0;
        using pack = vector<int>;
        vector<vector<int>> d = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        priority_queue<pack, vector<pack>, greater<pack>> heap;
        heap.push({0, 0, 0});
        while (heap.size())
        {
            auto top = heap.top();
            int times = top[0], x = top[1], y = top[2];
            heap.pop();
            if (x == m - 1 && y == n - 1) return times;
            if (times > dis[x][y]) continue;
            for (int i = 0; i < d.size(); i ++ )
            {
                int nx = x + d[i][0], ny = y + d[i][1];
                if (nx >= 0 && nx < m && ny >= 0 && ny < n)
                {
                    int nxt_time = max(times, moveTime[nx][ny]) + (x + y) % 2 + 1;
                    if (nxt_time < dis[nx][ny])
                    {
                        dis[nx][ny] = nxt_time;
                        heap.emplace(vector<int>{nxt_time, nx, ny});
                    }
                }
            }
        }
        return -1;
    }
};
// @lc code=end

