#
# @lc app=leetcode.cn id=3461 lang=python3
#
# [3461] 判断操作后字符串中的数字是否相等 I
#
from mytools import *
# @lc code=start
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            cur = ""
            for ch1, ch2 in pairwise(s):
                cur += str((int(ch1) + int(ch2)) % 10)
            s = cur
            
        if s[0] == s[1]: return True
        return False
# @lc code=end

