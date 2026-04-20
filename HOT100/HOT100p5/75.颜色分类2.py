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
        idx1 = idx2 = 0
        n = len(nums)
        for i in range(n):
            tmp = nums[i]
            nums[i] = 0
            if tmp == 0: idx1 += 1; idx2 += 1
            if tmp == 1: idx2 += 1
        for l in range(idx1, idx2):
            nums[l] = 1
        for r in range(idx2, n):
            nums[r] = 2
# @lc code=end

