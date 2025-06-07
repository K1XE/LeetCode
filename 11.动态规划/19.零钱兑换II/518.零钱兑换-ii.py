#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
from mytools import *
# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for j in range(amount + 1):
                if j >= c:
                    dp[j] += dp[j - c]
        return dp[amount]
# @lc code=end
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1): dp[i][0] = 1
        for i, c in enumerate(coins):
            for j in range(amount + 1):
                dp[i + 1][j] = dp[i][j]
                if j >= c:
                    dp[i + 1][j] += dp[i + 1][j - c]
        return dp[n][amount]
