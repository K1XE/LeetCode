#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
from mytools import *
# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums
    def heap_sort(self, nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1): self.heapify_(nums, n, i)
        for i in range(n - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify_(nums, i, 0)
    def heapify_(self, nums, n, i):
        while True:
            largest = i
            l, r = 2 * i + 1, 2 * i + 2
            if l < n and nums[l] > nums[largest]: largest = l
            if r < n and nums[r] > nums[largest]: largest = r
            if largest == i: break
            nums[i], nums[largest] = nums[largest], nums[i]
            i = largest
        
            
# @lc code=end

