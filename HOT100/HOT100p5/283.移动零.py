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
        idx = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0: continue
            nums[idx] = nums[i]; idx += 1
        for i in range(idx, n): nums[i] = 0
# @lc code=end

