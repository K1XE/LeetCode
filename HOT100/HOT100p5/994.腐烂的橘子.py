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
        d = (1, 0), (-1, 0), (0, 1), (0, -1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        cnt = 0
        l = len(q)
        res = 0
        f = False
        while q:
            f = True
            x, y = q.popleft()
            for nx, ny in d:
                dx, dy = x + nx, y + ny
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1:
                    grid[dx][dy] = 2
                    q.append((dx, dy))
            cnt += 1
            if cnt == l: res += 1; cnt = 0; l = len(q)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
        return res - 1 if f else 0
# @lc code=end

