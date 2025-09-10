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
        ll, rr = height[0], height[n - 1]
        l, r = 0, n - 1
        res = 0
        while l < r:
            ll = max(ll, height[l])
            rr = max(rr, height[r])
            if height[l] < height[r]:
                res += ll - height[l]; l += 1
            else: res += rr - height[r]; r -= 1
        return res
# @lc code=end

