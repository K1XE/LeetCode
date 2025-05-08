#
# @lc app=leetcode.cn id=3342 lang=python3
#
# [3342] 到达最后一个房间的最少时间 II
#
from mytools import *
# @lc code=start
class Solution:
    def minTimeToReach(self, g: List[List[int]]) -> int:
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(g), len(g[0])
        dis = [[float('inf')] * n for _ in range(m)]
        h = [(0, 0, 0)]
        dis[0][0] = 0
        heapq.heapify(h)
        while h:
            times, x, y = heapq.heappop(h)
            if x == m - 1 and y == n - 1: return times
            if times > dis[x][y]: continue
            for dx, dy in d:
                nx, ny = dx + x, dy + y
                if 0 <= nx < m and 0 <= ny < n:
                    nxt_time = max(g[nx][ny], times) + (x + y) % 2 + 1
                    if nxt_time < dis[nx][ny]:
                        dis[nx][ny] = nxt_time
                        heapq.heappush(h, (nxt_time, nx, ny))

# @lc code=end

