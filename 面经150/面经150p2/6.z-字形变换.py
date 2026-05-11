#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
from mytools import *
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        n = len(s)
        r = 0
        f = True
        if numRows == 1: return s
        for i in range(n):
            res[r].append(s[i])
            if (r == numRows - 1 or r == 0) and i != 0: f = not f
            r = r + (1 if f else -1)
        return "".join(["".join(st) for st in res])
# @lc code=end

