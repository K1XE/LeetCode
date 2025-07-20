#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
from typing import List
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for cnt in range(n):
            for i in range(cnt, n): matrix[i][cnt], matrix[cnt][i] = matrix[cnt][i], matrix[i][cnt]
        for row in matrix: row.reverse()
# @lc code=end

