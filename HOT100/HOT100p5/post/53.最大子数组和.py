#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from mytools import *
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = -inf
        s = 0
        for i in range(n):
            s += nums[i]
            res = max(res, s)
            if s < 0: s = 0
        return res
# @lc code=end

