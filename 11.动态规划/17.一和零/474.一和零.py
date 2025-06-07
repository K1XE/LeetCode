#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
from mytools import *
# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for i in range(1, len(strs) + 1):
            zero, one = strs[i - 1].count('0'), strs[i - 1].count('1')
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if zero <= j and one <= k:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - zero][k - one] + 1)
        return dp[len(strs)][m][n]
# @lc code=end
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zero = s.count('0')
            one = s.count('1')
            for j in range(m, zero - 1, -1):
                for k in range(n, one - 1, - 1):
                    dp[j][k] = max(dp[j][k], dp[j - zero][k - one] + 1)
        return dp[m][n]
