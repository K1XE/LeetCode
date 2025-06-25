#
# @lc app=leetcode.cn id=2040 lang=python3
#
# [2040] 两个有序数组的第 K 小乘积
#
from mytools import *
# @lc code=start
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def foo(x):
            cnt = 0
            n2 = len(nums2)
            for a in nums1:
                if a > 0:
                    b_ = x // a
                    cnt += bisect.bisect_right(nums2, b_)
                elif a < 0:
                    div, mod = divmod(x, a)
                    b_ = div + (1 if mod != 0 else 0)
                    cnt += n2 - bisect.bisect_left(nums2, b_)
                else:
                    if x >= 0: cnt += n2
            return cnt
        l, r = -10**10, 10**10
        while l < r:
            mid = l + r >> 1
            if foo(mid) < k:
                l = mid + 1
            else: r = mid
        return l
# @lc code=end

