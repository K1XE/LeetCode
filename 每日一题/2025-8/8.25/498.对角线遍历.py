#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#
from mytools import *
# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        for k in range(m + n - 1):
            min_j = max(k - m + 1, 0)
            max_j = min(k, n - 1)
            if k & 1:
                for j in range(max_j, min_j - 1, - 1):
                    res.append(mat[k - j][j])
            else:
                for j in range(min_j, max_j + 1):
                    res.append(mat[k - j][j])
        return res
# @lc code=end

