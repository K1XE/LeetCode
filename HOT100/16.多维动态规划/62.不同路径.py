#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
from mytools import *
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 0 x 1 y
        dp = [[[0] * 2 for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 1
        for i in range(m):
            for j in range(n):
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) if i - 1 >= 0 else dp[i][j][0]
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) if j - 1 >= 0 else dp[i][j][1]
        return sum(dp[m - 1][n - 1])
# @lc code=end

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 0 x 1 y
        dp = [[[0] * 2 for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = dp[0][0][1] = 1
        for i in range(m):
            for j in range(n):
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) if i - 1 >= 0 else dp[i][j][0]
                dp[i][j][1] = (dp[i][j - 1][0] + dp[i][j - 1][1]) if j - 1 >= 0 else dp[i][j][1]
        return sum(dp[m - 1][n - 1]) >> 1