#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from mytools import *
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minv = float("inf")
        res = 0
        for p in prices:
            minv = min(minv, p)
            res = max(p - minv, res)
        return res
# @lc code=end

