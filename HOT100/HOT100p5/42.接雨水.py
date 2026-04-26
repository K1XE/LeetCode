#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
from mytools import *
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        if n <= 1: return res
        lm, rm = height[0], height[-1]
        l, r = 0, n - 1
        while l < r:
            if lm <= rm:
                l += 1
                lm = max(height[l], lm)
                res += lm - height[l]
            else:
                r -= 1
                rm = max(height[r], rm)
                res += rm - height[r]
        return res
# @lc code=end
