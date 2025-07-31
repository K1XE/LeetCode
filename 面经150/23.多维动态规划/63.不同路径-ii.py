#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
from mytools import *
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] == 1: continue
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]
# @lc code=end

