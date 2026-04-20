#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
from mytools import *
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for x in coins:
            for j in range(x, amount + 1):
                dp[j] = min(dp[j], dp[j - x] + 1)
        return dp[-1] if dp[-1] != inf else -1
# @lc code=end

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[inf] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1): dp[i][0] = 0
        for i in range(1, n + 1):
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]: dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i - 1]] + 1)
        return dp[-1][amount] if dp[n][amount] != inf else -1