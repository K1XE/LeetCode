#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from mytools import *
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d = (0, 1), (1, 0), (0, -1), (-1, 0)
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            for dx, dy in d:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                    grid[nx][ny] = "#"
                    dfs(nx, ny)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "#"
                    dfs(i, j)
                    res += 1
        return res
# @lc code=end

