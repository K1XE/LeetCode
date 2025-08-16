#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
from typing import List


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for r in range(n):
            for l in range(r + 1):
                sub = s[l : r + 1]
                dp[0][r] |= (dp[0][l - 1] if l - 1 >= 0 else 1) & (sub in wordDict)
        return bool(dp[0][n - 1])


# @lc code=end
