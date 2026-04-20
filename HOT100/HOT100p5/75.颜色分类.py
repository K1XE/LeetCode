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
        if len(nums) <= 1:
            return
        idx1 = idx2 = 0

        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = 0
            if tmp == 0:
                idx1 += 1
                idx2 += 1
            if tmp == 1:
                idx2 += 1
        for l in range(idx1, idx2):
            nums[l] = 1
        for r in range(idx2, len(nums)):
            nums[r] = 2


# @lc code=end
