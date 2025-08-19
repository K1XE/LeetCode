#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
from mytools import *
# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [inf] * (n + 1)
        dp[0] = 0
        sqr = [i * i for i in range(1, int(n ** 0.5) + 1)]
        for x in range(1, n + 1):
            for sq in sqr:
                if sq > x: break
                dp[x] = min(dp[x], dp[x - sq] + 1)
        return dp[n]
# @lc code=end

