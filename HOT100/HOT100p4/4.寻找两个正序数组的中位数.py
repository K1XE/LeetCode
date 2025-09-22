#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from mytools import *
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        def foo(nums1, i, nums2, j, k):
            n1 = len(nums1) - i; n2 = len(nums2) - j
            if n1 > n2: return foo(nums2, j, nums1, i, k)
            if i == len(nums1): return nums2[j + k - 1]
            if k == 1: return min(nums1[i], nums2[j])
            idx1 = min(len(nums1), i + k // 2)
            idx2 = j + k - k // 2
            if nums1[idx1 - 1] > nums2[idx2 - 1]: return foo(nums1, i, nums2, idx2, k - (idx2 - j))
            else: return foo(nums1, idx1, nums2, j, k - (idx1 - i))
        if n & 1: return foo(nums1, 0, nums2, 0, (n >> 1) + 1)
        else: return (foo(nums1, 0, nums2, 0, n >> 1) + foo(nums1, 0, nums2, 0, (n >> 1) + 1)) / 2.0
        
# @lc code=end

