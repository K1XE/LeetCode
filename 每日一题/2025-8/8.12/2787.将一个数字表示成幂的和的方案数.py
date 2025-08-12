#
# @lc app=leetcode.cn id=2787 lang=python3
#
# [2787] 将一个数字表示成幂的和的方案数
#
from mytools import *
# @lc code=start
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [1] + [0] * n
        mod = 10**9 + 7
        for i in range(1, n + 1):
            v = i ** x
            if v > n: break
            for j in range(n, v - 1, -1):
                dp[j] += dp[j - v]
        return dp[n] % mod
# @lc code=end

