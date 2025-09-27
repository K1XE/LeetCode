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
        dp = [[False] * n for _ in range(n)]
        for i in range(n): dp[i][i] = True
        sta, eds = 0, 0
        for r in range(n):
            for l in range(r, -1, -1):
                if r - l <= 2: dp[l][r] |= s[l] == s[r]
                else: dp[l][r] |= s[l] == s[r] and dp[l + 1][r - 1]
                if dp[l][r] and r - l > eds - sta: sta, eds = l, r
        return s[sta:eds + 1]
# @lc code=end

