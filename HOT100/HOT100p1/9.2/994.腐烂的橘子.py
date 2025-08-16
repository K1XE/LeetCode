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
        vis = [[False] * n for _ in range(m)]
        dir = (1, 0), (-1, 0), (0, 1), (0, -1)
        q = deque()
        f = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    vis[i][j] = True
        res = -1
        while q:
            for _ in range(len(q)):
                tx, ty = q.popleft()
                for dx, dy in dir:
                    nx, ny = tx + dx, ty + dy
                    if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny] and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        vis[nx][ny] = True
                        q.append((nx, ny))
            res += 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1
        return max(0, res)
# @lc code=end

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dir = (1, 0), (-1, 0), (0, 1), (0, -1)
        q = deque()
        f = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: q.append((i, j))
                elif grid[i][j] == 1: f += 1
        def bfs():
            nonlocal f
            res = 0
            while q and f > 0:
                for _ in range(len(q)):
                    tx, ty = q.popleft()
                    for dx, dy in dir:
                        nx, ny = tx + dx, ty + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            f -= 1
                            q.append((nx, ny))
                res += 1
            return res if f == 0 else -1
        return bfs()