#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from mytools import * 
# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        if not points: return 0
        res = 1
        n = len(points)
        for i in range(1, n):
            if points[i][0] > points[i - 1][1]:
                res += 1
            else:
                points[i][1] = min(points[i][1], points[i - 1][1])
        return res
# @lc code=end

