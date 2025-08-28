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
        dp = [[0] * n for _ in range(n)]
        eds = -inf
        sta = inf
        for i in range(n): dp[i][i] = 1
        for r in range(n):
            for l in range(r, -1, -1):
                if r - l + 1 <= 3:
                    if s[l] == s[r]: dp[l][r] |= 1
                else:
                    if s[l] == s[r]: dp[l][r] |= dp[l + 1][r - 1]
                    
                if dp[l][r] and r - l > eds - sta: eds = r; sta = l
        return s[sta:eds + 1]
# @lc code=end

