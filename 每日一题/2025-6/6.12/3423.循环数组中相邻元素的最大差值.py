#
# @lc app=leetcode.cn id=3423 lang=python3
#
# [3423] 循环数组中相邻元素的最大差值
#
from mytools import *
# @lc code=start
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            diff = abs(nums[i] - nums[(i + 1) % n])
            res = max(res, diff)
        return res
# @lc code=end

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        res = 0
        for i in range(1, len(nums)):
            diff = abs(nums[i] - nums[i - 1])
            res = max(diff, res)
        return res