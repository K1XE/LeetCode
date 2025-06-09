#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
from mytools import *
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for j in range(c, amount + 1):
                dp[j] = min(dp[j], dp[j - c] + 1)
        return -1 if dp[amount] == amount + 1 else dp[amount]
# @lc code=end

