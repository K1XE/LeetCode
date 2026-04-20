#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
from mytools import *
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n <= 1: return 0
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
                else:
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                        dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
        return max(dp)
# @lc code=end

