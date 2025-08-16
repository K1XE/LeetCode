#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
from mytools import *
# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]
# @lc code=end

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * i for i in range(1, n + 1)]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            for j in range(i + 1):
                a = dp[i - 1][j - 1] + triangle[i][j] if j - 1 >= 0 else inf
                b = dp[i - 1][j] + triangle[i][j] if j < i else inf
                dp[i][j] = min(a, b)
        return min(dp[n - 1])
            
        