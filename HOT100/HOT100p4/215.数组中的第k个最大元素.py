#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from mytools import *
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def foo(nums, k):
            piv = choice(nums)
            l, m, r = [], [], []
            for x in nums:
                if x < piv: l.append(x)
                elif x == piv: m.append(x)
                else: r.append(x)
            if k <= len(r): return foo(r, k)
            elif k > len(r) + len(m): return foo(l, k - (len(r) + len(m)))
            else: return piv
        return foo(nums, k)
# @lc code=end

