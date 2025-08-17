#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from typing import List
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        if n % 2 == 1: return self.se(nums1, nums2, 0, 0, n // 2 + 1)
        else: return (self.se(nums1, nums2, 0, 0, n // 2) + self.se(nums1, nums2, 0, 0, n // 2 + 1)) / 2  
    def se(self, nums1, nums2, i, j, k):
        if len(nums1) - i > len(nums2) - j: return self.se(nums2, nums1, j, i, k)
        if i == len(nums1): return nums2[j + k - 1]
        if k == 1: return min(nums1[i], nums2[j])
        idx2 = j + k // 2
        idx1 = min(len(nums1), i + k - k // 2)
        if nums1[idx1 - 1] > nums2[idx2 - 1]: return self.se(nums1, nums2, i, idx2, k - (idx2 - j))
        else: return self.se(nums1, nums2, idx1, j, k - (idx1 - i))
        
# @lc code=end

