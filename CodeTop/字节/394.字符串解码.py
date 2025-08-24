#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
from mytools import *
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        nxt_num = 0
        cur = ""
        stk = []
        for ch in s:
            if ch.isdigit(): nxt_num = 10 * nxt_num + int(ch)
            elif ch == '[':
                stk.append((cur, nxt_num))
                cur = ""
                nxt_num = 0
            elif ch == ']':
                laxt, cur_num = stk.pop()
                cur = laxt + cur * cur_num 
            else: cur += ch
        return cur
# @lc code=end

