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
        if n == 1: return res
        lm, rm = height[0], height[-1]
        l, r = 0, n - 1
        while l <= r:
            if lm < rm:
                res += max(0, lm - height[l])
                lm = max(lm, height[l])
                l += 1
            else:
                res += max(0, rm - height[r])
                rm = max(rm, height[r])
                r -= 1
        return res
# @lc code=end

