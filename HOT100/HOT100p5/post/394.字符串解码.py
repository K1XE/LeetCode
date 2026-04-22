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
            elif ch.isalpha(): res += ch
            elif ch == "[": stk.append((res, num)); res = ""; num = 0
            else: prestr, curnum = stk.pop(); res = prestr + curnum * res
        # while stk:
        #     prestr, curnum = stk.pop()
        #     res = prestr + curnum * res
        return res
# @lc code=end

