#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
from mytools import *
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            rows = [1] * (i + 1)
            for j in range(1, i):
                rows[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(rows)
        return res
# @lc code=end

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * x for x in range(1, numRows + 1)]
        for i in range(numRows):
            for j in range(i): 
                res[i][j] = (res[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0) + res[i - 1][j] if i - 1 >= 0 and j < i else 0
        return res