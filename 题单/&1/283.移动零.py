#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
from mytools import *
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0
        for i in range(n):
            nums[j] = nums[i]
            if nums[j] != 0: j += 1
        for k in range(j, n): nums[k] = 0
# @lc code=end

