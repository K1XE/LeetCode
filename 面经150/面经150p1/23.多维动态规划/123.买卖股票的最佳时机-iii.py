#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
from mytools import *
# @lc code=start
# 0 : 0 n
# 1 : 0 y
# 2 : 1 n
# 3 : 1 y
# 4 : 1 n
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-inf] * 5 for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][0] - prices[i - 1], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i - 1])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i - 1])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i - 1])
        return max(dp[n])
# @lc code=end

