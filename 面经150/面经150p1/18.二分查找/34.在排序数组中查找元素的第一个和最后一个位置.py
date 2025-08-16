#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from mytools import *
# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(find_l: bool):
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                mid = l + r >> 1
                if nums[mid] == target:
                    res = mid
                    if find_l: r = mid - 1
                    else: l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else: l = mid + 1
            return res
        l = find(True)
        if l == -1: return [-1, -1]
        r = find(False)
        return [l, r]
        
# @lc code=end

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ll, rr = -1, -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] >= target: r = mid - 1
            else: l = mid + 1
        ll = l if 0 <= l < len(nums) and nums[l] == target else -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + r >> 1
            if nums[mid] <= target: l = mid + 1
            else: r = mid - 1
        rr = r if 0 <= r < len(nums) and nums[r] == target else -1
        return [-1, -1] if ll == -1 or rr == -1 else [ll, rr]