#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
from mytools import *
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        f = ["(", "[", "{"]
        for ch in s:
            if ch in f: stk.append(ch)
            else:
                if not stk: return False
                if ch == ")": 
                    if stk[-1] != "(": return False
                    else: stk.pop()
                elif ch == "]":
                    if stk[-1] != "[": return False
                    else: stk.pop()
                else:
                    if stk[-1] != "{": return False
                    else: stk.pop()
        return not stk
# @lc code=end

