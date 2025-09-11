#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#
from mytools import *
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
# @lc code=end

