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
        for i in range(n):
            if s[i] == ")": 
                if i > 0:
                    if s[i - 1] == "(": dp[i] = 2 + (dp[i - 2] if i - 2 >= 0 else 0)
                    else:
                        x = i - dp[i - 1] - 1
                        if x >= 0 and s[x] == "(":
                            dp[i] = dp[i - 1] + 2 + (dp[x - 1] if x - 1 >= 0 else 0)
        return max(dp)
# @lc code=end

