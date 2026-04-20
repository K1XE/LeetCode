#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
from mytools import *
# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]
        for i in range(1, l1 + 1): dp[0][i] = i
        for i in range(1, l2 + 1): dp[i][0] = i
        for i in range(0, l2):
            for j in range(0, l1):
                if word1[j] == word2[i]: dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
        return dp[-1][-1]
# @lc code=end

