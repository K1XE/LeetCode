#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
from mytools import *
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): dp[i][0] = i
        for j in range(n + 1): dp[0][j] = j
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]: dp[i + 1][j + 1] = dp[i][j]
                else: dp[i + 1][j + 1] = min(
                    dp[i][j + 1] + 1,
                    dp[i + 1][j] + 1,
                    dp[i][j] + 1
                )
        return dp[m][n]
# @lc code=end

