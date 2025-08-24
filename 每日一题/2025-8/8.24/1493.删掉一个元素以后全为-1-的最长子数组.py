#
# @lc app=leetcode.cn id=1493 lang=python3
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#
from mytools import *


# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = cnt0 = l = 0
        for r, x in enumerate(nums):
            cnt0 += 1 - x
            while cnt0 > 1:
                cnt0 -= 1 - nums[l]
                l += 1
            res = max(res, r - l)
        return res


# @lc code=end
