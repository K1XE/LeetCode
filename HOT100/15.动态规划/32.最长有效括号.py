#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
from mytools import *
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
                elif dp[i - 1] > 0:
                    j = i - dp[i - 1] - 1
                    if j >= 0 and s[j] == '(':
                        dp[i] = dp[i - 1] + 2
                        if j - 1 >= 0: dp[i] += dp[j - 1]
                    
        return max(dp)
# @lc code=end

