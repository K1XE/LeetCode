#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
from mytools import *
# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x > 0 and x % 10 == 0: return False
        rev = 0
        while rev < x // 10:
            rev = rev * 10 + x % 10
            x //= 10
        return rev == x or rev == x // 10
# @lc code=end

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        s = str(x)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for r in range(n):
            for l in range(r, -1, -1):
                if r - l + 1 <= 3: dp[l][r] |= s[l] == s[r]
                else:
                    dp[l][r] |= dp[l + 1][r - 1] and s[l] == s[r]
        return dp[0][n - 1]