#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#
from mytools import *
# @lc code=start
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3
            return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        n = len(points)
        res = -1
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    res = max(res, area(points[i], points[j], points[k]))
        return res
# @lc code=end

