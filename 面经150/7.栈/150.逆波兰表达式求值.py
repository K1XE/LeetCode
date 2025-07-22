#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
from typing import List
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t.lstrip("+-").isdigit(): stk.append(int(t))
            else:
                a, b = stk.pop(), stk.pop()
                if t == '+': stk.append(b + a)
                elif t == '-': stk.append(b - a)
                elif t == '*': stk.append(b * a)
                else: stk.append(int(b / a))
        return stk[-1]
# @lc code=end

