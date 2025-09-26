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
        if n == 0: return 0
        dp = [0] * n
        for i, ch in enumerate(s):
            if ch == ")":
                if i > 0:
                    if s[i - 1] == "(": dp[i] = (dp[i - 2] if i - 2 >= 0 else 0) + 2
                    else:
                        idx = i - dp[i - 1] - 1
                        if idx >= 0 and s[idx] == "(":
                            dp[i] = 2 + dp[i - 1] + (dp[idx - 1] if idx - 1 >= 0 else 0)
        return max(dp)
# @lc code=end

