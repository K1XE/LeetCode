#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
from mytools import *
# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        b = [x for x in range(1, n + 1) if (x**0.5).is_integer()]
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for x in b:
                if x > i: break
                dp[i] = min(dp[i], dp[i - x] + 1)
        return dp[n]
# @lc code=end

