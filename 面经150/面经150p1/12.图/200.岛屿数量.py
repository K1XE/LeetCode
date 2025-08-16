#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from typing import List
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = (1, 0), (-1, 0), (0, 1), (0, -1)
        res = 0
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            grid[x][y] = "0"
            for dx, dy in dir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1": dfs(nx, ny)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1": res += 1; dfs(i, j)
        return res
# @lc code=end

