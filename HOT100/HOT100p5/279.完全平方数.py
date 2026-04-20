#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
from mytools import *
# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        max_ = int(n ** 0.5)
        dp = [inf] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, max_ + 1):
            for j in range(i ** 2, n + 1):
                dp[j] = min(dp[j], dp[j - i ** 2] + 1)
        return dp[n]
# @lc code=end

