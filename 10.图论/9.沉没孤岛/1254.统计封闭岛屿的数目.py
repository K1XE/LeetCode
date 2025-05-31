#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#
from mytools import *
# @lc code=start
class Solution:
    def closedIsland(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])
        d = [[1, 0], [-1 ,0], [0, 1], [0, -1]]
        def dfs(x, y):
            g[x][y] = 7
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and g[nx][ny] == 0:
                    dfs(nx, ny)
        for i in range(m):
            if g[i][0] == 0: dfs(i, 0)
            if g[i][n - 1] == 0: dfs(i, n -1)
        for j in range(n):
            if g[0][j] == 0: dfs(0, j)
            if g[m - 1][j] == 0: dfs(m - 1, j)
        res = 0
        for i in range(m):
            for j in range(n):
                if g[i][j] == 0:
                    res += 1
                    dfs(i, j)
        return res
# @lc code=end

