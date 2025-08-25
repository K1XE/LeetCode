#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
from mytools import *
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        pre = suf = -1
        res = 0
        while l < r:
            pre = max(pre, height[l])
            suf = max(suf, height[r])
            if pre > suf:
                res += suf - height[r]
                r -= 1
            else:
                res += pre - height[l]
                l += 1
        return res
# @lc code=end

