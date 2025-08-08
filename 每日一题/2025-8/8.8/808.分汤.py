#
# @lc app=leetcode.cn id=808 lang=python3
#
# [808] 分汤
#
from mytools import *
# @lc code=start
class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4551: return 1.0
        m = (n + 24) // 25
        dp = [[0.0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 0.5
        for j in range(1, m + 1): dp[0][j] = 1.0
        for i in range(1, m + 1): dp[i][0] = 0.0
        for i in range(1, m + 1):
            for j in range(1, m + 1):
                dp[i][j] = (
                    dp[max(0, i - 4)][j] +
                    dp[max(0, i - 3)][max(0, j - 1)] +
                    dp[max(0, i - 2)][max(0, j - 2)] + 
                    dp[max(0, i - 1)][max(0, j - 3)]
                ) / 4.0
        return dp[m][m]
# @lc code=end

