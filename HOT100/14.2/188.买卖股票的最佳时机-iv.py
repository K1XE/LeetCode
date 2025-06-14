#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
from mytools import *
# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * (2 * k + 1) for _ in range(n) ]
        dp[0][0] = 0
        for i in range(1, 2 * k + 1, 2):
            dp[0][i] = -prices[0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0]
            for j in range(1, 2 * k + 1, 2):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] + prices[i])
        return max(dp[n - 1])
# @lc code=end

