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
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]) if i - 1 >= 0 else 0
            dp[i][1] = max(dp[i - 1][1] if i - 1 >= 0 else -inf, -prices[i])
        return dp[-1][0]
# @lc code=end

