#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
from mytools import *
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        x = 0
        cur = ""
        stk = []
        for ch in s:
            if ch.isdigit(): x = x * 10 + int(ch)
            elif ch.isalpha(): cur += ch
            elif ch == "[": stk.append((x, cur)); x = 0; cur = ""
            else: xt, curt = stk.pop(); cur = curt + xt * cur
        return cur
# @lc code=end

