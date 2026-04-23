#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from mytools import *
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        res = 0
        d = (1, 0), (-1, 0), (0, 1), (0, -1)
        m, n = len(grid), len(grid[0])
        def bfs():
            nonlocal res
            res += 1
            while q:
                x, y = q.popleft()
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                        grid[nx][ny] = "K"
                        q.append((nx, ny))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "K"
                    q.append((i, j))
                    bfs()

        return res
# @lc code=end

