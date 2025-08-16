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
        sta, res = 0, 1
        dp = [[False] * n for _ in range(n)]
        for i in range(n): dp[i][i] = True
        for l in range(n - 1, -1, -1):
            for r in range(l + 1, n):
                if s[l] == s[r]:
                    if r - l == 1: dp[l][r] = True
                    else: dp[l][r] = dp[l + 1][r - 1]
                else: dp[l][r] = False
                if dp[l][r] and r - l + 1 > res:
                    res = r - l + 1
                    sta = l
        return s[sta:sta + res]

# @lc code=end

