#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#
from mytools import *
# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n > 0) & (n & (n - 1) == 0)
# @lc code=end

