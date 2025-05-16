#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pair = {'(' : ')', '[' : ']', '{' : '}'}
        for ch in s:
            if ch in pair:
                stk.append(ch)
            elif ch in pair.values():
                if not stk or pair[stk[-1]] != ch: return False
                stk.pop()
            else: return False
        return not stk
# @lc code=end

