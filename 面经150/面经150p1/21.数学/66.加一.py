#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
from mytools import *
# @lc code=start

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            x = digits[i] + 1
            if x < 10: digits[i] = x; break
            else: digits[i] = 0
        if digits[0] == 0: digits.insert(0, 1)
        return digits
# @lc code=end

