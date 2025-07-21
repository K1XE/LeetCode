#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
from typing import List
# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        cur = points[0]
        cnt = 1
        for p in points[1:]:
            if p[0] <= cur[1]: cur[1] = min(cur[1], p[1])
            else: cur = p; cnt += 1
        return cnt
# @lc code=end

