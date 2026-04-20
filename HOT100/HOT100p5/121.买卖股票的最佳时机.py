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
        if n <= 1: return 0
        f1 = f2 = False
        res = 0
        cur = prices[0]
        for i in range(1, n):
            res = max(res, prices[i] - cur)
            cur = min(prices[i], cur)
        return res
# @lc code=end

