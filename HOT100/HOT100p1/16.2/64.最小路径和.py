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
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = dp[0][1] = dp[1][0] = 0
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
        return dp[m][n]
# @lc code=end

