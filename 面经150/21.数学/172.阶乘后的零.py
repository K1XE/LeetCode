#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
from mytools import *
# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            n //= 5
            res += n
        return res
# @lc code=end

