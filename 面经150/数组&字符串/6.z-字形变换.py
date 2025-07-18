#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
from mytools import *
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, f = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: f = - f
            i += f
        return ''.join(res)
# @lc code=end

