#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
from mytools import *
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = dp[1][0] = 0.5
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]
        return int(dp[m][n])
# @lc code=end

