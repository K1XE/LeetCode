#
# @lc app=leetcode.cn id=2197 lang=python3
#
# [2197] 替换数组中的非互质数
#
from mytools import *
# @lc code=start
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stk = []
        for x in nums:
            while stk and gcd(x, stk[-1]) > 1:
                x = lcm(x, stk.pop())
            stk.append(x)
        return stk
# @lc code=end

