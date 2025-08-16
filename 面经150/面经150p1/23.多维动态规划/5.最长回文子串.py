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
        sta = eds = 0
        for r in range(n):
            for l in range(r - 1, -1, -1):
                if r - l <= 2: dp[l][r] = s[l] == s[r]
                else: dp[l][r] = dp[l + 1][r - 1] and s[l] == s[r]
                if dp[l][r] and r - l + 1 >= eds - sta + 1: sta, eds = l, r
        return s[sta:eds + 1]
# @lc code=end

