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
        i = 0
        for j in range(n):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for k in range(i, n): nums[k] = 0
# @lc code=end

