#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from mytools import *
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        def dfs(nums1, i, nums2, j, k):
            if len(nums2) - j < len(nums1) - i:
                return dfs(nums2, j, nums1, i, k)
            if i == len(nums1): return nums2[j + k - 1]
            if k == 1:
                return min(nums1[i], nums2[j])
            idx1 = min(len(nums1), i + k // 2)
            idx2 = j + k - k // 2
            if nums1[idx1 - 1] > nums2[idx2 - 1]:
                return dfs(nums1, i, nums2, idx2, k - (idx2 - j))
            else: return dfs(nums1, idx1, nums2, j, k - (idx1 - i))

        if n % 2 == 1: return dfs(nums1, 0, nums2, 0, n // 2 + 1)
        else:
            l = dfs(nums1, 0, nums2, 0, n // 2)
            r = dfs(nums1, 0, nums2, 0, n // 2 + 1)
            return (l + r) / 2.0

        
# @lc code=end

