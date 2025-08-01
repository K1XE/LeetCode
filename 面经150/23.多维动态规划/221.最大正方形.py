 #
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
from mytools import *
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i + 1][j + 1] = min(
                        dp[i][j],
                        dp[i + 1][j],
                        dp[i][j + 1] 
                    ) + 1
                    res = max(res, dp[i + 1][j + 1])
        return res * res
# @lc code=end

