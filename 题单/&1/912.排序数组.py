#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
from mytools import *
# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums
    def quicksort(self, nums, l, r):
        if l >= r: return
        i, j = l - 1, r + 1
        piv = nums[randint(l, r)]
        while i < j:
            i += 1
            while nums[i] < piv: i += 1
            j -= 1
            while nums[j] > piv: j -= 1
            if i < j: nums[i], nums[j] = nums[j], nums[i]
        self.quicksort(nums, l, j)
        self.quicksort(nums, j + 1, r)
    
        
# @lc code=end

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heapsort(nums)
        
    def heapsort(self, nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_(nums, i, n)
        for i in range(n - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify_(nums, 0, i)
        return nums

    def heapify_(self, nums, i, n):
        while True:
            largest = i
            l = 2 * i + 1; r = 2 * i + 2
            if l < n and nums[l] > nums[largest]: largest = l
            if r < n and nums[r] > nums[largest]: largest = r
            if largest == i: break
            nums[largest], nums[i] = nums[i], nums[largest]
            i = largest
            