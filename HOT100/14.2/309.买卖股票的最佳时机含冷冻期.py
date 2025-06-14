#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#
from mytools import *
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 0: do anything 1: nothing and freeze 2: nothing but can buy 3: already buy
        dp = [[0] * 4 for _ in range(n)]
        dp[0][3] = -prices[0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = dp[i - 1][3] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][0])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i], dp[i - 1][0] - prices[i])
        return max(dp[n - 1])
# @lc code=end

