#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from typing import List
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        def find(nums1, idx1, nums2, idx2, k):
            if len(nums1) - idx1 > len(nums2) - idx2: return find(nums2, idx2, nums1, idx1, k)
            if idx1 == len(nums1): return nums2[idx2 + k - 1]
            if k == 1: return min(nums1[idx1], nums2[idx2])
            nxt2 = idx2 + (k >> 1)
            nxt1 = min(len(nums1), idx1 + k - (k >> 1))
            if nums1[nxt1 - 1] < nums2[nxt2 - 1]: return find(nums1, nxt1, nums2, idx2, k - (nxt1 - idx1))
            else: return find(nums1, idx1, nums2, nxt2, k - (nxt2 - idx2))
        if n & 1: return find(nums1, 0, nums2, 0, (n >> 1) + 1)
        else: return (find(nums1, 0, nums2, 0, n >> 1) + find(nums1, 0, nums2, 0, (n >> 1) + 1)) / 2
# @lc code=end

