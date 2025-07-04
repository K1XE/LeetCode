#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from mytools import *
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0; r = len(height) - 1
        res = 0
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] > height[r]: r -= 1
            else: l += 1
        return res
# @lc code=end

