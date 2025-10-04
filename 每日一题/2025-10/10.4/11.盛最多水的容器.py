#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
from mytools import *
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        l = 0; r = n - 1
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[r] < height[l]: r -= 1
            else: l += 1
        return res
# @lc code=end

