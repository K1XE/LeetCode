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
        matrix[:] = [list(m[::-1]) for m in zip(*matrix)]
# @lc code=end

