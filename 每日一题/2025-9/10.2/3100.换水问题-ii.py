#
# @lc app=leetcode.cn id=3100 lang=python3
#
# [3100] 换水问题 II
#
from mytools import *
# @lc code=start
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        while numBottles >= numExchange:
            res += numExchange
            numBottles -= numExchange - 1
            numExchange += 1
        return res + numBottles
# @lc code=end

