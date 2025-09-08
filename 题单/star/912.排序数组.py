#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
from mytools import *
# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums
    def quick_sort(self, nums, l, r):
        if l >= r: return
        i = l - 1; j = r + 1
        piv = nums[randint(l, r)]
        while i < j:
            i += 1
            while nums[i] < piv: i += 1
            j -= 1
            while nums[j] > piv: j -= 1
            if i < j: nums[i], nums[j] = nums[j], nums[i]
        self.quick_sort(nums, l, j)
        self.quick_sort(nums, j + 1, r)
        
# @lc code=end
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heap_sort(nums)
        return nums
    def heap_sort(self, nums):
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_(nums, n, i)
        for i in range(n - 1, -1, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify_(nums, i, 0)
    def heapify_(self, nums, n, i):
        while True:
            lar = i
            if 2 * i + 1 < n and nums[2 * i + 1] > nums[lar]: lar = 2 * i + 1
            if 2 * i + 2 < n and nums[2 * i + 2] > nums[lar]: lar = 2 * i + 2
            if lar == i: break
            nums[lar], nums[i] = nums[i], nums[lar]
            i = lar
        
