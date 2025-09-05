#
# @lc app=leetcode.cn id=2749 lang=python3
#
# [2749] 得到整数零需要执行的最少操作数
#
from mytools import *
# @lc code=start
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in count(1):
            x = num1 - num2 * k
            if k > x: return -1
            if k >= x.bit_count(): return k
        
# @lc code=end

