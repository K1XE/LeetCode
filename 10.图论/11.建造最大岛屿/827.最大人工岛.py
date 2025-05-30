#
# @lc app=leetcode.cn id=827 lang=python3
#
# [827] 最大人工岛
#
from mytools import *
# @lc code=start
class Solution:
    def largestIsland(self, g: List[List[int]]) -> int:
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(g), len(g[0])
        vis = [[False] * n for _ in range(m)]
        mk = 2
        def dfs(x, y, mk):
            vis[x][y] = 1
            area = 1
            g[x][y] = mk
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny] and g[nx][ny] != 0:
                    area += dfs(nx, ny, mk)
            return area
        hash = defaultdict(int)
        ff = True
        for i in range(m):
            for j in range(n):
                if g[i][j] == 0: ff = False
                if g[i][j] != 0 and not vis[i][j]:
                    area = dfs(i, j, mk)
                    hash[mk] = area
                    mk += 1
        if ff: return m * n
        res = 0
        for i in range(m):
            for j in range(n):
                if g[i][j] == 0:
                    ss = set()
                    cur = 1
                    for dx, dy in d:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n and g[ni][nj] != 0 and g[ni][nj] not in ss:
                            cur += hash[g[ni][nj]]
                            ss.add(g[ni][nj])
                    res = max(res, cur)
        return res
# @lc code=end

