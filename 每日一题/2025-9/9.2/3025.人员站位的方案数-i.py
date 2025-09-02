#
# @lc app=leetcode.cn id=3025 lang=python3
#
# [3025] 人员站位的方案数 I
#
from mytools import *
# @lc code=start
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        for i, (_, y1) in enumerate(points):
            maxy = -inf
            for _, y2 in points[i + 1:]:
                if maxy < y2 <= y1: maxy = y2; res += 1
        return res
# @lc code=end

