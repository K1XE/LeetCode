#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
from mytools import *
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0] * (i + 1) for i in range(numRows)]
        dp[0][0] = 1
        for i in range(1, numRows):
            for j in range(i + 1):
                dp[i][j] = (dp[i - 1][j - 1] if j - 1 >= 0 else 0) + (dp[i - 1][j] if j < i else 0)
        return dp
# @lc code=end

