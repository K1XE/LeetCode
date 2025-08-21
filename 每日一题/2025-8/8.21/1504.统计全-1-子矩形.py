#
# @lc app=leetcode.cn id=1504 lang=python3
#
# [1504] 统计全 1 子矩形
#
from mytools import *


# @lc code=start
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        res = 0
        for top in range(m):
            a = [0] * n
            for bottom in range(top, m):
                last = -1
                h = bottom - top + 1
                for j in range(n):
                    a[j] += mat[bottom][j]
                    if a[j] != h:
                        last = j
                    else:
                        res += j - last
        return res


# @lc code=end
