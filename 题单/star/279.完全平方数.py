#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
from mytools import *
# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        back = [x for x in range(1, n + 1) if sqrt(x).is_integer()]
        dp = [inf] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, n + 1):
            for b in back:
                
                if b > i: break
                if i == b: dp[i] = 1
                else: dp[i] = min(dp[i], dp[i - b] + 1)
        return dp[n]
            
# @lc code=end

