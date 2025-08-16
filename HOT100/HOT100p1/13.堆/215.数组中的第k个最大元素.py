#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
import random
from mytools import *
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quick_select(uu, k):
            l, e, r = [], [], []
            piv = random.choice(uu)
            for x in uu:
                if piv > x:
                    l.append(x)
                elif piv == x:
                    e.append(x)
                else:
                    r.append(x)
            if k <= len(r):
                return quick_select(r, k)
            elif len(r) + len(e) < k:
                return quick_select(l, k - (len(r) + len(e)))
            else: return piv
        
        return quick_select(nums, k)

# @lc code=end

