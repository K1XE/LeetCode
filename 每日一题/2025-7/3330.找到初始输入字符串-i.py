#
# @lc app=leetcode.cn id=3330 lang=python3
#
# [3330] 找到初始输入字符串 I
#
from mytools import *
# @lc code=start
class Solution:
    def possibleStringCount(self, word: str) -> int:
        return sum(x == y for x, y in pairwise(word)) + 1
# @lc code=end

class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        res = 1
        for i in range(1, n):
            if word[i] == word[i - 1]: res += 1
        return res