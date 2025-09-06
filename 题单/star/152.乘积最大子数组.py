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
        dpmin = [inf] * n
        dpmax = [-inf] * n
        dpmin[0] = dpmax[0] = nums[0]
        for i in range(1, n):
            dpmin[i] = min(dpmin[i - 1] * nums[i], dpmax[i - 1] * nums[i], nums[i])
            dpmax[i] = max(dpmin[i - 1] * nums[i], dpmax[i - 1] * nums[i], nums[i])
        return max(dpmax)
# @lc code=end

