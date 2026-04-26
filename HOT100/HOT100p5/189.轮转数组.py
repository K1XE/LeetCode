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
        n = len(nums)
        k %= n
        nums[:-k] = reversed(nums[:-k])
        nums[-k:] = reversed(nums[-k:])
        nums[:] = reversed(nums)
# @lc code=end

