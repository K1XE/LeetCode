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
        d = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = deque()
        fr = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1: fr += 1
        def bfs():
            nonlocal fr
            res = 0
            while q and fr > 0:
                for _ in range(len(q)):
                    u, v = q.popleft()
                    for dx, dy in d:
                        nx, ny = u + dx, v + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fr -= 1
                            q.append((nx, ny))
                res += 1
            return -1 if fr > 0 else res
        return bfs()
# @lc code=end

