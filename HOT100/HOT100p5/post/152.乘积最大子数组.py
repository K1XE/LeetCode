#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
from mytools import *
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dpmin = [0] * n
        dpmax = [0] * n
        dpmin[0] = dpmax[0] = nums[0]
        for i in range(1, n):
            dpmin[i] = min(nums[i], dpmax[i - 1] * nums[i], dpmin[i - 1] * nums[i])
            dpmax[i] = max(nums[i], dpmin[i - 1] * nums[i], dpmax[i - 1] * nums[i])
        return max(dpmax)
# @lc code=end

