#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
inf = float("inf")
from typing import List
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        minl, maxl = inf, 0
        for w in wordDict:
            minl = min(minl, len(w))
            maxl = max(maxl, len(w))
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n + 1):
            for l in range(minl, min(maxl, i) + 1):
                if dp[i - l] and s[i - l:i] in wordset:
                    dp[i] = True
                    break
        return dp[n]
# @lc code=end
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        minl = inf
        for s1 in wordDict: minl = min(minl, len(s1))
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n + 1):
            for j in range(1, i + 1):
                if s[j - 1:i] in wordDict: dp[i] |= dp[j - 1]
        return dp[n]
