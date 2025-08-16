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
        l, r = 0, n - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return r
# @lc code=end

