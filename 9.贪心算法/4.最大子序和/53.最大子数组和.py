#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from mytools import *
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if tmp > res:
                res = tmp
            if tmp < 0: tmp = 0
        return res
# @lc code=end

