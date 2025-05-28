#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
from mytools import *
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]
        def dfs(x, y):
            for i in range(4):
                (nx, ny) = (x + d[i][0], y + d[i][1])
                if (0 <= nx < m and 0 <= ny < n and not vis[nx][ny] and grid[nx][ny] == '1'):
                    vis[nx][ny] = True
                    dfs(nx, ny)

        res = 0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res

# @lc code=end

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        vis = [[False] * n for _ in range(m)]
        def bfs(x, y):
            q = deque()
            q.append((x, y))
            nonlocal vis
            vis[x][y] = True
            while q:
                u, v = q.popleft()
                for i in range(4):
                    (nx, ny) = (u + d[i][0], v + d[i][1])
                    if (0 <= nx < m and 0 <= ny < n and not vis[nx][ny] and grid[nx][ny] == '1'):
                        vis[nx][ny] = True
                        q.append((nx, ny))
        res = 0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == '1':
                    res += 1
                    bfs(i, j)
        return res

