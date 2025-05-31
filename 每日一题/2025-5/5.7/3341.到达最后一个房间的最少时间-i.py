#
# @lc app=leetcode.cn id=3341 lang=python3
#
# [3341] 到达最后一个房间的最少时间 I
#
from mytools import *
# @lc code=start
class Solution:
    def minTimeToReach(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        vis = [[float('inf')] * n for _ in range(m)]
        h = [(0, 0, 0)]
        vis[0][0] = 0
        while True:
            i, j, times = heapq.heappop(h)
            if i == m - 1 and j == n - 1: return times
            if times > vis[i][j]: continue
            for dx, dy in d:
                ni, nj = dx + i, dy + j
                if 0 <= ni < m and 0 <= nj < n:
                    nxt_time = max(times, g[ni][nj]) + 1
                    if nxt_time < vis[ni][nj]:
                        vis[ni][nj] = nxt_time
                        heapq.heappush(h, (ni, nj, nxt_time))


# @lc code=end

