#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#
from mytools import *
# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                return nums[i - 2] + nums[i - 1] + nums[i]
        return 0
# @lc code=end

