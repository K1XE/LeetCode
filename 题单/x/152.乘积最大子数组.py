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
        dpmax = [1] * (n + 1)
        dpmin = [1] * (n + 1)
        for i in range(n):
            dpmax[i + 1] = max(nums[i], nums[i] * dpmax[i], nums[i] * dpmin[i])
            dpmin[i + 1] = min(nums[i], nums[i] * dpmin[i], nums[i] * dpmax[i])
        return max(dpmax[1:])
# @lc code=end

