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
        m, n = len(matrix), len(matrix[0])
        flagl, flagh = False, False
        for i in range(m):
            if matrix[i][0] == 0:
                flagl = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                flagh = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i] = [0] * n
        for j in range(1, n):
            if matrix[0][j] == 0:
                for u in range(m):
                    matrix[u][j] = 0
        if flagl:
            for u in range(m):
                matrix[u][0] = 0
        if flagh:
            matrix[0] = [0] * n


# @lc code=end

