#
# @lc app=leetcode.cn id=3027 lang=python3
#
# [3027] 人员站位的方案数 II
#
from mytools import *
# @lc code=start
class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))  # x 升序，y 降序
        ans = 0
        for i, (_, y1) in enumerate(points):
            max_y = -inf
            for (_, y2) in points[i + 1:]:
                if y1 >= y2 > max_y:
                    max_y = y2
                    ans += 1
                if max_y == y1:  # 优化
                    break
        return ans
# @lc code=end

