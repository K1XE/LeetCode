#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        sta = eds = 0
        for r in range(n):
            for l in range(r):
                if r - l <= 2: dp[l][r] |= s[l] == s[r]
                else:
                    dp[l][r] |= (s[l] == s[r]) & dp[l + 1][r - 1]
                if dp[l][r] and r - l > eds - sta: eds = r; sta = l
        return s[sta:eds + 1]
                    
# @lc code=end

