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
        resl, resr = -1, -1
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]: l -= 1; r += 1
            return l + 1, r - 1
        for i in range(n):
            l, r = max([expand(i, i), expand(i, i + 1)], key=lambda p: p[1] - p[0])
            if r - l >= resr - resl: resr, resl = r, l
        return s[resl:resr + 1]

# @lc code=end

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resl, resr = -1, -1
        dp = [[False] * n for _ in range(n)]
        for i in range(n): dp[i][i] = True
        for r in range(n):
            for l in range(r, -1, -1):
                if r - l + 1 <= 3: dp[l][r] |= s[l] == s[r]
                else:
                    dp[l][r] = dp[l + 1][r - 1] & (s[l] == s[r])
                if dp[l][r] and r - l >= resr - resl:
                    resl, resr = l, r
        print(resl, resr)
        return s[resl:resr + 1]