#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
from mytools import *
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        h, l = False, False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                h = True
        for j in range(n):
            if matrix[0][j] == 0:
                l = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if h: 
            for i in range(m): matrix[i][0] = 0
        if l:
            for j in range(n): matrix[0][j] = 0
# @lc code=end

