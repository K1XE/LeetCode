#
# @lc app=leetcode.cn id=2257 lang=python3
#
# [2257] 统计网格图中没有被保卫的格子数
#
from mytools import *
# @lc code=start
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        b = [[0] * n for _ in range(m)]
        dir = (0, 1), (0, -1), (1, 0), (-1, 0)
        for x, y in guards: b[x][y] = -1
        for x, y in walls: b[x][y] = -1
        for x, y in guards:
            for dx, dy in dir:
                nx = x + dx; ny = y + dy
                while 0 <= nx < m and 0 <= ny < n and b[nx][ny] != -1:
                    b[nx][ny] = 1
                    nx += dx
                    ny += dy
        return sum(row.count(0) for row in b)
            
# @lc code=end

