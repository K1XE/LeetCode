#
# @lc app=leetcode.cn id=2439 lang=python3
#
# [2439] 最小化数组中的最大值
#
from mytools import *
# @lc code=start
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        def ck(x):
            cur = 0
            for i in range(n - 1, 0, -1):
                cur = max(0, nums[i] + cur - x)
            return nums[0] + cur <= x
        l, r = min(nums), max(nums)
        while l < r:
            mid = l + r >> 1
            if ck(mid): r = mid
            else: l = mid + 1
        return r
# @lc code=end

