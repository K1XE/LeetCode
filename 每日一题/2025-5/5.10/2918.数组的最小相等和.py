#
# @lc app=leetcode.cn id=2918 lang=python3
#
# [2918] 数组的最小相等和
#
from mytools import *
# @lc code=start
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(max(x, 1) for x in nums1)
        sum2 = sum(max(x, 1) for x in nums2)
        if sum1 > sum2 and 0 not in nums2\
            or sum2 > sum1 and 0 not in nums1:
            return -1
        return max(sum1, sum2)


# @lc code=end

# ......
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        n1, n2 = len(nums1), len(nums2)
        cnt1, cnt2 = 0, 0
        diff = sum1 - sum2
        for i in range(n1):
            if nums1[i] == 0: cnt1 += 1
        for i in range(n2):
            if nums2[i] == 0: cnt2 += 1
        print(sum1, sum2, cnt1, cnt2)
        if diff > 0:
            if cnt2 == 0: return -1
            elif cnt1 == 0 and sum2 + cnt2 > sum1: return -1
            return max(sum1 + cnt1, sum2 + cnt2)
        elif diff < 0:
            if cnt1 == 0: return -1
            elif cnt2 == 0 and sum1 + cnt1 > sum2: return - 1
            return max(sum1 + cnt1, sum2 + cnt2)
        else:
            if cnt1 != 0 and cnt2 == 0: return -1
            if cnt2 != 0 and cnt1 == 0: return -1
            return sum1 + max(cnt1, cnt2)