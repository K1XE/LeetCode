#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from typing import *
inf = float("inf")
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = cur = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            res = max(res, cur)
        return res
            
# @lc code=end

