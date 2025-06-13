#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from mytools import *
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 0 x 1 y
        m, n = len(grid), len(grid[0])
        dp = [[[inf] * 2 for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = dp[0][0][1] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i > 0: dp[i][j][0] = min((min(dp[i - 1][j][0], dp[i - 1][j][1])) + grid[i][j], dp[i][j][0])
                if j > 0: dp[i][j][1] = min((min(dp[i][j - 1][0], dp[i][j - 1][1])) + grid[i][j], dp[i][j][1])
        return min(dp[m - 1][n - 1])
# @lc code=end

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 0 x 1 y
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]