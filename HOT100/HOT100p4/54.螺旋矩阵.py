#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
from mytools import *
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, r, t, b = 0, n - 1, 0, m - 1
        res = []
        while True:
            for j in range(l, r + 1): res.append(matrix[t][j])
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r])
            r -= 1
            if l > r: break
            for j in range(r, l - 1, -1): res.append(matrix[b][j])
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l])
            l += 1
            if l > r: break
        return res
# @lc code=end

