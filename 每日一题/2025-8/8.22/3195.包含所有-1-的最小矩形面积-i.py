#
# @lc app=leetcode.cn id=3195 lang=python3
#
# [3195] 包含所有 1 的最小矩形面积 I
#
from mytools import *
# @lc code=start
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_row = min_col = inf
        max_row = max_col = -inf
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)
        
        return (max_row - min_row + 1) * (max_col - min_col + 1)
        
        
# @lc code=end

