#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        res = 0
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i + 1] = dp[i - 1] + 2
                else:
                    if i - dp[i] - 1 >= 0 and s[i - dp[i] - 1] == "(": dp[i + 1] = 2 + dp[i] + dp[i - dp[i] - 1]
            res = max(res, dp[i + 1])
        return res
# @lc code=end

