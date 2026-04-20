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
            elif ch == "[": stk.append((res, num)); num = 0; res = ""
            else:
                pre_s, cur_num = stk.pop()
                res = pre_s + cur_num * res
        return res
        
# @lc code=end

