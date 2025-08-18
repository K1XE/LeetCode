#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
from mytools import *
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums0 = nums01 = 0
        for i in range(len(nums)):
            tmp = nums[i]
            if tmp == 0: nums0 += 1; nums01 += 1
            if tmp == 1: nums01 += 1
        for i in range(nums0): nums[i] = 0
        for i in range(nums0, nums01): nums[i] = 1
        for i in range(nums01, len(nums)): nums[i] = 2
        
# @lc code=end

