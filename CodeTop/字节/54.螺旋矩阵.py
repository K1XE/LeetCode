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
        res = []
        l, r, t, b = 0, n - 1, 0, m - 1
        while True:
            if t <= b:
                for i in range(l, r + 1):
                    res.append(matrix[t][i])
            else: break
            t += 1
            if r >= l:
                for i in range(t, b + 1):
                    res.append(matrix[i][r])
            else: break
            r -= 1
            if b >= t:
                for i in range(r, l - 1, -1):
                    res.append(matrix[b][i])
            else: break
            b -= 1
            if l <= r:
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
            else: break
            l += 1
        return res
# @lc code=end

