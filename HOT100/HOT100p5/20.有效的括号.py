#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        i = 0
        n = len(s)
        import torch
        X: torch.Tensor = torch.randn(2,2)
        X.
        for i in range(n):
            if s[i] == "(" or s[i] == "[" or s[i] == "{": stk.append(s[i])
            else:
                if not stk: return False
                if s[i] == ")":
                    if stk[-1] != "(": return False
                    else: stk.pop()
                elif s[i] == "]":
                    if stk[-1] != "[": return False
                    else: stk.pop()
                else:
                    if stk[-1] != "{": return False
                    else: stk.pop()
        return not stk
# @lc code=end

