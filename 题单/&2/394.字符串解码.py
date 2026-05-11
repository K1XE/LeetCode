#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
from mytools import *
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        num = 0
        stk = []
        for ch in s:
            if ch.isdigit(): num = num * 10 + int(ch)
            if ch.isalpha(): res += ch
            if ch == "[": stk.append((res, num)); res = ""; num = 0
            if ch == "]": pres, curn = stk.pop(); res = pres + curn * res
        return res
# @lc code=end

