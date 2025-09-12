#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#
from mytools import *
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target: return True
            elif matrix[i][j] > target: j -= 1
            else: i += 1
            
# @lc code=end

