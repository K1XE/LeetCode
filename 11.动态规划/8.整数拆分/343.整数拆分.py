#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
from mytools import *
# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        return dp[n]
# @lc code=end

