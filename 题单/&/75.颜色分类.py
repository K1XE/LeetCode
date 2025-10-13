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
        for i, x in enumerate(nums):
            tmp = x
            if tmp <= 1: nums[cnt01] = 1; cnt01 += 1
            if tmp == 0: nums[cnt0] = 0; cnt0 += 1
        for i in range(cnt01, len(nums)):
            nums[i] = 2
# @lc code=end

