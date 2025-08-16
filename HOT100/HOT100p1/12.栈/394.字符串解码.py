#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
from mytools import *
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        cur_str = ''
        nxt_num = 0
        for ch in s:
            if ch.isdigit():
                nxt_num = nxt_num * 10 + int(ch)
            elif ch == '[':
                stk.append((cur_str, nxt_num))
                cur_str = ''
                nxt_num = 0
            elif ch == ']':
                last_str, cur_num = stk.pop()
                cur_str = last_str + cur_str * cur_num
            else:
                cur_str += ch
        return cur_str
                

# @lc code=end

