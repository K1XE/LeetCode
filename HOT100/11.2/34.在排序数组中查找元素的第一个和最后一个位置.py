#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from mytools import *
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ll, rr = -1, n
        l, r = 0, n - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        ll = l
        l, r = 0, n - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        rr = r
        return [ll, rr] if ll <= rr and nums[ll] == target else [-1, -1]
# @lc code=end

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ll, rr = -1, n
        l, r = 0, n - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        rr = l
        l, r = 0, n - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        ll = r
        return [ll + 1, rr - 1] if ll + 1 <= rr - 1 and nums[ll + 1] == target else [-1, -1]
