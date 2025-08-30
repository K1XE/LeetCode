#
# @lc app=leetcode.cn id=678 lang=python3
#
# [678] 有效的括号字符串
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        l = h = 0
        for ch in s:
            if ch == "(": l += 1; h += 1
            elif ch == ")": l = max(l - 1, 0); h -= 1
            else: l = max(l - 1, 0); h += 1
            if h < 0: return False
        return l == 0
# @lc code=end

