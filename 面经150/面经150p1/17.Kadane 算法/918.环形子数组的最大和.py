#
# @lc app=leetcode.cn id=918 lang=python3
#
# [918] 环形子数组的最大和
#
from typing import List
inf = float("inf")
# @lc code=start
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s, curmax, resmax, curmin, resmin = 0, 0, nums[0], 0, nums[0]
        for x in nums:
            curmax = max(curmax + x, x)
            resmax = max(resmax, curmax)
            curmin = min(curmin + x, x)
            resmin = min(resmin, curmin)
            s += x
        return max(resmax, s - resmin) if resmax > 0 else resmax
# @lc code=end

