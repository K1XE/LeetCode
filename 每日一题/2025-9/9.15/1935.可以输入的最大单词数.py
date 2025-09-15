#
# @lc app=leetcode.cn id=1935 lang=python3
#
# [1935] 可以输入的最大单词数
#
from mytools import *
# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        n = len(text)
        i = 0
        cnt = 0
        while i < n:
            f = True
            while i < n and text[i] != " ": 
                ch = text[i]
                if ch in brokenLetters: f = False
                i += 1
            if f: cnt += 1
            i += 1
        return cnt
# @lc code=end

