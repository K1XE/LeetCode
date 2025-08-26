#
# @lc app=leetcode.cn id=3000 lang=python3
#
# [3000] 对角线最长的矩形的面积
#
from mytools import *
# @lc code=start
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_ = 0
        res = 0
        for a, b in dimensions:
            tmp = sqrt(a ** 2 + b ** 2)
            if tmp > max_:
                max_ = tmp
                res = a * b
            elif tmp == max_: res = max(res, a * b)
        return res
# @lc code=end

