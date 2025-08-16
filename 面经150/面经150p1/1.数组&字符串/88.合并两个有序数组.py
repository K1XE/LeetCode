#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
from mytools import *
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1; j = n - 1; k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while i >= 0:
            nums1[k] = nums1[i]
            k -= 1; i -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1; j -= 1
# @lc code=end

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = k = 0
        tmp = nums1[:]
        while i < m and j < n:
            if tmp[i] < nums2[j]:
                nums1[k] = tmp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while i < m:
            nums1[k] = tmp[i]
            k += 1; i += 1
        while j < n:
            nums1[k] = nums2[j]
            k += 1; j += 1