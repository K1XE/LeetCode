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
        dp = [[-inf] * (2 * k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for u in range(1, 2 * k + 1):
                dp[i][0] = dp[i - 1][0]
                if u & 1 == 1: dp[i][u] = max(dp[i - 1][u], dp[i - 1][u - 1] - prices[i - 1])
                else: dp[i][u] = max(dp[i - 1][u], dp[i - 1][u - 1] + prices[i - 1])
        return max(dp[n])

# @lc code=end

