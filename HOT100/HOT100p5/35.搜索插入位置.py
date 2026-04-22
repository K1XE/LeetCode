#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
from mytools import *
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] < target: l = mid + 1
            elif nums[mid] > target: r = mid - 1
            else: return mid
        return l
# @lc code=end

