#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from mytools import *
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def sch(nums, k):
            pivot = random.choice(nums)
            l, m, r = [], [], []
            for x in nums:
                if x < pivot: l.append(x)
                elif x == pivot: m.append(x)
                else: r.append(x)
            if k <= len(r): return sch(r, k)
            elif k > len(r) + len(m): return sch(l, k - (len(r) + len(m)))
            else: return pivot
        return sch(nums, k)
# @lc code=end

