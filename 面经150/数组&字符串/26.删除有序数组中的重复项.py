#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#
from mytools import *
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        idx = 0
        i = 0
        while i < n:
            nums[idx] = nums[i]
            idx += 1; i += 1
            while i < n and nums[i] == nums[i - 1]: i += 1
        return idx
# @lc code=end

