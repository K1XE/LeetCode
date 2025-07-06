#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
from mytools import *
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxl = 0
        sta, eds = 0,0
        dp = [[False] * (n) for _ in range(n)]
        for i in range(n): dp[i][i] = True
        for j in range(n):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i <= 1: dp[i][j] = True
                    else: dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and j - i + 1 > maxl:
                    maxl = j - i + 1
                    sta, eds = i, j
        return s[sta:eds + 1]

# @lc code=end

