#
# @lc app=leetcode.cn id=3446 lang=python3
#
# [3446] 按对角线进行矩阵排序
#
from mytools import *
# @lc code=start
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        pack = []
        for u in range(n):
            i = u; j = 0
            pack.clear()
            while i < n and j < n: pack.append(grid[i][j]); i += 1; j += 1
            pack.sort(reverse=True)
            i = u; j = 0
            cnt = 0
            while i < n and j < n: grid[i][j] = pack[cnt]; i += 1; j += 1; cnt += 1
        for u in range(1, n):
            i = 0; j = u
            pack.clear()
            while i < n and j < n: pack.append(grid[i][j]); i += 1; j += 1
            pack.sort()
            i = 0; j = u
            cnt = 0
            while i < n and j < n: grid[i][j] = pack[cnt]; i += 1; j += 1; cnt += 1
        return grid
            
# @lc code=end

