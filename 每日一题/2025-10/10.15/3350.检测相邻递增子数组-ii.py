#
# @lc app=leetcode.cn id=3350 lang=python3
#
# [3350] 检测相邻递增子数组 II
#
from mytools import *
# @lc code=start
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res = pre = cnt = 0
        for i, x in enumerate(nums):
            cnt += 1
            if i == len(nums) - 1 or x >= nums[i + 1]:
                res = max(res, min(pre, cnt), cnt // 2)
                pre = cnt
                cnt = 0
        return res
# @lc code=end

