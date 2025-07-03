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

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            if nums[i] == 0: break
        sta = i
        for j in range(sta + 1, n):
            if nums[j] == 0: continue
            while i < j and nums[i] != 0: i += 1
            nums[i], nums[j] = nums[j], nums[i]