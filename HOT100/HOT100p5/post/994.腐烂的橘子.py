#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
from mytools import *
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = (1, 0), (-1, 0), (0, 1), (0, -1)
        q = deque()
        f = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: f = True
                if grid[i][j] == 2:
                    q.append((i, j))
        if not q and not f: return 0
        res = 0
        while q:
            l = len(q)
            for _ in range(l):
                x, y = q.popleft()
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
            res += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
        return res - 1
# @lc code=end

