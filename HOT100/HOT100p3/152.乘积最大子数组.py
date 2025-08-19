#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
from mytools import *
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_ = max_ = res = nums[0]
        for x in nums[1:]:
            max_, min_ = max(x, max_ * x, min_ * x), min(x, min_ * x, max_ * x)
            res = max(res, max_)
        return res
# @lc code=end

