#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
from mytools import *
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        n = len(s)
        res = ["" for _ in range(numRows)]
        d = True
        idx = 0
        for i in range(n):
            res[idx] += s[i]
            if d:
                if idx == numRows - 1: d = False; idx -= 1
                else: idx += 1
            else:
                if idx == 0: d = True; idx += 1
                else: idx -= 1
        return "".join(res)


# @lc code=end

