#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
from mytools import *
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for r in range(n):
            for l in range(r + 1):
                dp[0][r] |= (dp[0][l - 1] if l - 1 >= 0 else True) and s[l : r + 1] in wordDict
        return dp[0][-1]
# @lc code=end

