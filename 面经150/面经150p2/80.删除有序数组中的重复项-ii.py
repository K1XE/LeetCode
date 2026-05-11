#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#
from mytools import *
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2: return n
        i = idx = 1
        while i < n:
            if nums[i] == nums[i - 1]:
                nums[idx] = nums[i]; idx += 1
                while i < n and nums[i] == nums[i - 1]: i += 1
                if i < n: nums[idx] = nums[i]; idx += 1; i += 1
            else:
                nums[idx] = nums[i]; idx += 1; i += 1
        return idx
# @lc code=end

