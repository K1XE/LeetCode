#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
from mytools import *
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: q.append((i, j)); vis[i][j] = True
                elif grid[i][j] == 1: cnt += 1
        if cnt == 0: return 0
        res = 0
        d = (0, 1), (1, 0), (0, -1), (-1, 0)
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny] and grid[nx][ny] == 1:
                        vis[nx][ny] = True
                        grid[nx][ny] = 2
                        q.append((nx, ny))
            res += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
        return res - 1
# @lc code=end

