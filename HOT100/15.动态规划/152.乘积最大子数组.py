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
        dp_max = dp_min = res = nums[0]
        for x in nums[1:]:
            dp_min, dp_max = min(dp_max * x, dp_min * x, x), max(dp_max * x, dp_min * x, x)
            res = max(res, dp_max)
        return res
# @lc code=end

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_min = [0] * n
        dp_max = [0] * n
        dp_max[0] = dp_min[0] = nums[0]
        for i in range(1, n):
            dp_max[i] = max(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i], nums[i])
            dp_min[i] = min(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i], nums[i])
        return max(dp_max)