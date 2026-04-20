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
        dp = [[inf] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = grid[i][0] + (dp[i - 1][0] if i - 1 >= 0 else 0)
        for j in range(n):
            dp[0][j] = grid[0][j] + (dp[0][j - 1] if j - 1 >= 0 else 0)
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
        return dp[-1][-1]
# @lc code=end

