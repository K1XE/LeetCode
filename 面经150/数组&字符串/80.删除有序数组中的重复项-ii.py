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
        idx = 2
        for i in range(2, n):
            if nums[i] != nums[idx - 2]:
                nums[idx] = nums[i]
                idx += 1
        return idx

# @lc code=end

