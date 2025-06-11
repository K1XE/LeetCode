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
        if n == 0 or k == 0: return 0
        if k >= n // 2: return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))
        dp = [[0] * (2 * k + 1) for _ in range(n)]
        for i in range(1, 2 * k + 1, 2):
            dp[0][i] = -prices[0]
        for i in range(1, n):
            for j in range(1, 2 * k + 1, 2):
                dp[i][j] = max(dp[i - 1][j - 1] - prices[i], dp[i - 1][j])
                dp[i][j + 1] = max(dp[i - 1][j] + prices[i], dp[i - 1][j + 1])
        return dp[n - 1][2 * k]
# @lc code=end

