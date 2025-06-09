#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
from mytools import *
# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, n + 1):
            if not math.sqrt(i).is_integer(): continue
            for j in range(i, n + 1):
                dp[j] = min(dp[j], dp[j - i] + 1)
        return dp[n]
# @lc code=end

