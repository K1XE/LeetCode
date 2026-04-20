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
        if n == 1: return nums[0]
        dpmax = [0] * (n + 1)
        dpmin = [0] * (n + 1)
        dpmax[1] = dpmin[1] = 1
        for i in range(n):
            dpmax[i + 1] = max(dpmax[i] * nums[i], dpmin[i] * nums[i], nums[i])
            dpmin[i + 1] = min(dpmax[i] * nums[i], dpmin[i] * nums[i], nums[i])
        return max(dpmax)
# @lc code=end

