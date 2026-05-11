#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
from mytools import *
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        ss = ""
        stk = []
        for ch in s:
            if ch.isdigit(): num = num * 10 + int(ch)
            elif ch.isalpha(): ss += ch
            elif ch == "[": stk.append((num, ss)); num = 0; ss = ""
            else: cur_num, pre_s = stk.pop(); ss = pre_s + cur_num * ss
            print(ss)
        return ss
# @lc code=end

