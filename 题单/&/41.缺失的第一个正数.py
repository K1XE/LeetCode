#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
from mytools import *
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]: nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i, x in enumerate(nums):
            if x != i + 1: return i + 1
        return len(nums) + 1
# @lc code=end

