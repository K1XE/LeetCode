#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from mytools import *
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1); n2 = len(nums2)
        n = n1 + n2
        def f(nums1, nums2, idx1, idx2, k):
            n1 = len(nums1) - idx1; n2 = len(nums2) - idx2;
            if n1 > n2: return f(nums2, nums1, idx2, idx1, k)
            if idx1 == len(nums1): return nums2[idx2 + k - 1]
            if k == 1: return min(nums1[idx1], nums2[idx2])
            nxt1 = min(len(nums1), idx1 + k // 2)
            nxt2 = idx2 + k - k // 2
            if nums1[nxt1 - 1] > nums2[nxt2 - 1]: return f(nums1, nums2, idx1, nxt2, k - (nxt2 - idx2))
            else: return f(nums1, nums2, nxt1, idx2, k - (nxt1 - idx1))
        if n & 1: return f(nums1, nums2, 0, 0, (n >> 1) + 1)
        else: return (f(nums1, nums2, 0, 0, (n >> 1)) + f(nums1, nums2, 0, 0, (n >> 1) + 1)) / 2
            
# @lc code=end

