#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from mytools import *
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -inf
        n = len(nums)
        cur = 0
        for i in range(n):
            res = max(res, cur + nums[i])
            if cur + nums[i] <= 0: cur = 0
            else: cur += nums[i]
        return res
# @lc code=end

