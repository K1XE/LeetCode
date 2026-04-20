#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
from mytools import *
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            dp[i][1] = (dp[i - 2][0] + dp[i - 2][1]) if i - 2 >= 0 else 0
        return sum(dp[-1])
# @lc code=end

