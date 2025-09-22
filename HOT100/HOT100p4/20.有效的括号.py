#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
from mytools import *
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stk = []
        for i in range(n):
            if s[i] == ")":
                if not stk or stk[-1] != "(": return False
                else: stk.pop()
            elif s[i] == "]":
                if not stk or stk[-1] != "[": return False
                else: stk.pop()
            elif s[i] == "}":
                if not stk or stk[-1] != "{": return False
                else: stk.pop()
            else: stk.append(s[i])
        return True if not stk else False
# @lc code=end

