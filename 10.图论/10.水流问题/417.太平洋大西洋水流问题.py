#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#
from mytools import *
# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(heights), len(heights[0])
        vis1 = [[False] * n for _ in range(m)]
        vis2 = [[False] * n for _ in range(m)]
        def dfs(x, y, vis):
            vis[x][y] = 1
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and not vis[nx][ny]:
                    dfs(nx, ny, vis)
        for i in range(m):
            if not vis1[i][0]: dfs(i, 0, vis1)
            if not vis2[i][n - 1]: dfs(i, n - 1, vis2)
        for j in range(n):
            if not vis1[0][j]: dfs(0, j, vis1)
            if not vis2[m - 1][j]: dfs(m - 1, j, vis2)
        res = []
        for i in range(m):
            for j in range(n):
                if vis1[i][j] and vis2[i][j]: res.append([i, j])
        return res
# @lc code=end

