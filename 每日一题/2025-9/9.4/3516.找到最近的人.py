#
# @lc app=leetcode.cn id=3516 lang=python3
#
# [3516] 找到最近的人
#
from mytools import *
# @lc code=start
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1, d2 = abs(z - x), abs(z - y)
        if d1 == d2: return 0
        return 1 if d1 < d2 else 2
# @lc code=end

