#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
from mytools import *
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        cur = inf
        for i in range(n):
            cur = min(cur, prices[i])
            res = max(res, prices[i] - cur)
        return res
# @lc code=end

