#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
from mytools import *
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        d = 0
        ss = ""
        stk = []
        for ch in s:
            if ch.isdigit(): d = d * 10 + int(ch)
            elif ch.isalpha(): ss += ch
            elif ch == "[": stk.append((ss, d)); ss = ""; d = 0
            else:
                pres, pred = stk.pop()
                ss = pres + pred * ss
        return ss
# @lc code=end

