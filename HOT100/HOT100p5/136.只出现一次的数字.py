#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
from mytools import *
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for x in nums[1:]: res ^= x
        return res
# @lc code=end

