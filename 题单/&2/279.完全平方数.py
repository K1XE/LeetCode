#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
from mytools import *
# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        tar = int(n ** 0.5)
        dp = [inf] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for x in range(tar + 1):
            for j in range(x ** 2, n + 1):
                dp[j] = min(dp[j], dp[j - x ** 2] + 1)
        return dp[-1]
            
            
# @lc code=end

