#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
from typing import List
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * i for i in range(1, numRows + 1)]
        for i in range(1, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  
        return dp
# @lc code=end

