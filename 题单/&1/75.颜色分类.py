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
        cnt0 = cnt01 = 0
        n = len(nums)
        for x in nums:
            if x <= 1: nums[cnt01] = 1; cnt01 += 1
            if x == 0: nums[cnt0] = 0; cnt0 += 1
        for i in range(cnt01, n): nums[i] = 2
    
        """ 
        for i in range(n):
            cur = nums[i]
            if cur <= 1: nums[cnt01] = 1; cnt01 += 1
            if cur == 0: nums[cnt0] = 0; cnt0 += 1
        for i in range(cnt01, n): nums[i] = 2
         """
# @lc code=end

0