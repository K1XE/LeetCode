#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
from mytools import *
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        ss = ""
        num = 0
        stk = []
        for ch in s:
            if ch.isdigit():
                x = int(ch)
                num = num * 10 + x
            elif ch.isalpha():
                ss += ch
            elif ch == "[":
                stk.append((ss, num))
                ss = ""; num = 0
            else:
                sss, nums = stk.pop()
                ss = sss + nums * ss
        return ss
# @lc code=end

