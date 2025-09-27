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
        c0 = c01 = 0
        
        for x in nums:
            tmp = x
            x = 2
            if tmp <= 1:
                nums[c01] = 1
                c01 += 1
            if tmp == 0:
                nums[c0] = 0
                c0 += 1
        for i in range(c01, len(nums)): nums[i] = 2
# @lc code=end

