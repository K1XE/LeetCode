#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
from mytools import *
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + (dp[i - 2] if i - 2 >= 0 else 0)
        return dp[-1]
# @lc code=end

