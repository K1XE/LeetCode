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
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != inf else -1
# @lc code=end

