#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
from mytools import *
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx = n - 2
        while idx >= 0 and nums[idx] >= nums[idx + 1]: idx -= 1
        if idx < 0: nums.reverse(); return
        idx2 = n - 1
        while idx2 > idx and nums[idx] >= nums[idx2]: idx2 -= 1
        nums[idx], nums[idx2] = nums[idx2], nums[idx]
        l = idx + 1
        r = n - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1; l += 1
# @lc code=end

