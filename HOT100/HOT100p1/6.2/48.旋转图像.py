#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
from mytools import *
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        tmp =  [list(row)[::-1] for row in zip(*matrix)]
        matrix = tmp
# @lc code=end
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        cnt = 0
        while cnt < n:
            i, j = cnt, cnt
            for _ in range(n - cnt):
                matrix[i][cnt], matrix[cnt][j] = matrix[cnt][j], matrix[i][cnt]
                i += 1; j += 1
            cnt += 1
        l, r = 0, n - 1
        while l < r:
            for i in range(n):
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1