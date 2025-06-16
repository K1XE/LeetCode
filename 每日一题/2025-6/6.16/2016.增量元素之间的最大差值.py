#
# @lc app=leetcode.cn id=2016 lang=python3
#
# [2016] 增量元素之间的最大差值
#
from mytools import *
# @lc code=start
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    res = max(res, nums[i] - nums[j])
        return res
# @lc code=end

