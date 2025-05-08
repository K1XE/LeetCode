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
        l, r = 0, n - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] >= target: r = mid - 1
            else: l = mid + 1
        left = l
        
        l, r = 0, n - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] <= target: l = mid + 1
            else: r = mid - 1
        right = r

        if left >= n or right >= n or left < 0 or right < 0 or nums[left] != target or nums[right] != target:
            return [-1, -1]
        else: return [left, right]
# @lc code=end

