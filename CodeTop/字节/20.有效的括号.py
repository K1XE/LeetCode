#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch == '}':
                if not stk or stk[-1] != "{": return False
                else: stk.pop()
            elif ch == ")":
                if not stk or stk[-1] != "(": return False
                else: stk.pop()
            elif ch == "]":
                if not stk or stk[-1] != "[": return False
                else: stk.pop()
            else: stk.append(ch)
        return not stk
# @lc code=end

