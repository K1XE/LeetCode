#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from mytools import *
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minv = float("inf")
        res = 0
        for x in prices:
            minv = min(x, minv)
            res = max(res, x - minv)
        return res
# @lc code=end

