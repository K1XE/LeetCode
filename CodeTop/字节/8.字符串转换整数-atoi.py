#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        x = 0
        i = 0
        sign = 1
        s = s.strip()
        n = len(s)
        while i < n:
            if s[i] == " ": break
            elif s[i] == "+":
                if i > 0: break
            elif s[i] == "-":
                if i == 0: sign = -1
                else: break
            elif s[i].isdigit():
                x = 10 * x + sign * (ord(s[i]) - ord("0"))
                if not (-2**31 <= x <= 2**31 - 1): x = -2**31 if x < 0 else (2**31 - 1); break
            else: break
            i += 1
        return x

# @lc code=end

