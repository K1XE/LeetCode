#
# @lc app=leetcode.cn id=2131 lang=python3
#
# [2131] 连接两字母单词得到的最长回文串
#
from mytools import *
# @lc code=start
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        res = 0
        odd = 0
        for w, c in cnt.items():
            if w[0] == w[1]:
                res += c - c % 2
                odd |= c % 2
            elif w[0] < w[1]:
                res += min(c, cnt[w[::-1]]) * 2
        return (res + odd) * 2
# @lc code=end

