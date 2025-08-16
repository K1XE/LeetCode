#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
from mytools import *
# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i, (x, y) in enumerate(points):
            cnt = defaultdict(int)
            for nx, ny in points[i + 1:]:
                dx, dy = nx - x, ny - y
                k = dy / dx if dx else inf
                cnt[k] += 1
                res = max(res, cnt[k])
        return res + 1
# @lc code=end

