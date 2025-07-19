#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
from mytools import *
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j = 0
        n = len(nums)
        s = 0
        res = inf
        for i in range(n):
            s += nums[i]
            while j <= i and s >= target:
                res = min(res, i - j + 1)
                s -= nums[j]
                j += 1
        return res if res != inf else 0
# @lc code=end

