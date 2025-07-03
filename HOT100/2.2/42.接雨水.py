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
        pre_max, suf_max = 0, 0
        l, r = 0, n - 1
        while l < r:
            pre_max = max(pre_max, height[l])
            suf_max = max(suf_max, height[r])
            if pre_max < suf_max:
                res += pre_max - height[l]
                l += 1
            else:
                res += suf_max - height[r]
                r -= 1
        return res
# @lc code=end

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre = [-1] * n
        suf = [-1] * n
        for i in range(n):
            pre[i] = max(pre[i - 1] if i - 1 >= 0 else -1, height[i])
        for i in range(n - 1, -1, -1):
            suf[i] = max(suf[i + 1] if i + 1 <= n - 1 else - 1, height[i])
        res = 0
        for i in range(n):
            res += min(pre[i], suf[i]) - height[i]
        return res