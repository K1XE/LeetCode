#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
from mytools import *
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for x in nums:
            a, b = (a ^ x) & (a | b), (b ^ x) & (~a)
        return b
# @lc code=end

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(31):
            cnt = sum(x >> i & 1 for x in nums)
            res |= cnt % 3 << i
        cnt = sum(x >> 31 & 1 for x in nums)
        return res - (cnt % 3 << 31)