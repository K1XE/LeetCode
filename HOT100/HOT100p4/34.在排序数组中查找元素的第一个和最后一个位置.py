#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from mytools import *
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] >= target: r = mid - 1
            else: l = mid + 1
        if l < 0 or l >= len(nums) or nums[l] != target: return [-1, -1]
        ll = l
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] <= target: l = mid + 1
            else: r = mid - 1
        return [ll, r]
# @lc code=end

