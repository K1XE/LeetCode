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
        t0 = 0
        t01 = 0
        for x in nums:
            tmp = x
            x = 2
            if tmp <= 1:
                nums[t01] = 1
                t01 += 1
            if tmp == 0:
                nums[t0] = 0
                t0 += 1
        n = len(nums)
        for i in range(t01, n):
            nums[i] = 2
# @lc code=end

