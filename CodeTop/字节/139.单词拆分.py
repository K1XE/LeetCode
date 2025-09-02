#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
from mytools import *
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        minlen = min(len(x) for x in wordDict)
        maxlen = max(len(x) for x in wordDict)
        print(minlen)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(max(0, i - maxlen), i - minlen + 2):
                if s[j:i + 1] in wordDict:
                    if j == 0: dp[0][i] = True; break
                    else: dp[0][i] |= dp[0][j - 1]
        return dp[0][n - 1]
# @lc code=end

