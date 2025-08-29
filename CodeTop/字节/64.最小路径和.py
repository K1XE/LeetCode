#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from mytools import *
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1): dp[i][0] = dp[i - 1][0] + grid[i - 1][0]
        for j in range(1, n + 1): dp[0][j] = dp[0][j - 1] + grid[0][j - 1]
        dp[0][1] = dp[1][0] = 0
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
        return dp[m][n]
# @lc code=end

