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
        if n <= 1: return s
        dp = [[False] * n for _ in range(n)]
        resl = resr = -1
        for i in range(n):
            dp[i][i] = True
        for r in range(n):
            for l in range(r + 1):
                if r - l + 1 <= 3: dp[l][r] = s[l] == s[r]
                else: dp[l][r] = s[r] == s[l] and dp[l + 1][r - 1]
                if dp[l][r] and r - l >= resr - resl:
                    resr, resl = r, l
        return s[resl:resr + 1]
                
# @lc code=end

