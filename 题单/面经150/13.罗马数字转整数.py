#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
from mytools import *
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        res = 0
        hash = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        for i in range(n - 1):
            if hash[s[i]] < hash[s[i + 1]]:
                res -= hash[s[i]]
            else: res += hash[s[i]]
        return res + hash[s[-1]]
# @lc code=end

