#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        res = 0
        num = 0
        sign = 1
        n = len(s)
        i = 0
        while i < n:
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in "+-":
                res += sign * num
                num = 0
                sign = 1 if s[i] == '+' else -1
            elif s[i] == '(':
                stk.append(res)
                stk.append(sign)
                res = 0
                sign = 1
            elif s[i] == ')':
                res += sign * num
                num = 0
                res *= stk.pop()
                res += stk.pop()
            i += 1
        return res + sign * num
# @lc code=end

