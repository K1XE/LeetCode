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
        ok = [x for x in range(1, n + 1) if math.sqrt(x).is_integer()]
        dp[0] = 0
        for x in ok:
            for j in range(x, n + 1):
                dp[j] = min(dp[j], dp[j - x] + 1)

        return dp[n]
# @lc code=end

