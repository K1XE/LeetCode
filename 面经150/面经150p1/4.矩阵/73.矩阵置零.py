#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
from typing import List
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        f1 = f2 = False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                f1 = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                f2 = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n): matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m): matrix[i][j] = 0
        if f1:
            for i in range(m): matrix[i][0] = 0
        if f2:
            for j in range(n): matrix[0][j] = 0
# @lc code=end

