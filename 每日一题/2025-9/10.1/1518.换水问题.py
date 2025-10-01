#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换水问题
#
from mytools import *
# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            cur, nxt = divmod(numBottles, numExchange)
            numBottles = cur + nxt
            res += cur
        return res
# @lc code=end

