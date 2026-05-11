#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        h = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        n = len(s)
        res = 0
        for i in range(n):
            if i < n - 1:
                res = res + (h[s[i]] if h[s[i]] >= h[s[i + 1]] else (- h[s[i]]))
            else:
                res += h[s[i]]
        return res
        
# @lc code=end

