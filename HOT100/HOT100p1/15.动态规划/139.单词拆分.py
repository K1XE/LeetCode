#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
from mytools import *
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(map(len, wordDict))
        ss = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, - 1), -1):
                if dp[j] and s[j:i] in ss:
                    dp[i] = True
                    break
        return dp[n]
# @lc code=end

