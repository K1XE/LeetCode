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
        dp = grid
        for i in range(1, m): dp[i][0] += dp[i - 1][0]
        for j in range(1, n): dp[0][j] += dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                a = dp[i - 1][j] if i - 1 >= 0 else inf
                b = dp[i][j - 1] if j - 1 >= 0 else inf
                dp[i][j] = min(a, b) + grid[i][j]
        return dp[m - 1][n - 1]
# @lc code=end

