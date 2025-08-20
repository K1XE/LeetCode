#
# @lc app=leetcode.cn id=1277 lang=python3
#
# [1277] 统计全为 1 的正方形子矩阵
#
from mytools import *
# @lc code=start
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if matrix[i][j] == 1:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
        return sum(map(sum, dp))
# @lc code=end

