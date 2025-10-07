#
# @lc app=leetcode.cn id=1488 lang=python3
#
# [1488] 避免洪水泛滥
#
from mytools import *
# @lc code=start
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [-1] * n
        full = {}
        dry = SortedList()
        for i, r in enumerate(rains):
            if r == 0:
                res[i] = 1
                dry.add(i)
                continue
            if r in full:
                j = full[r]
                k = dry.bisect_right(j)
                if k == len(dry): return []
                d = dry[k]
                res[d] = r
                dry.discard(d)
            full[r] = i
        return res
# @lc code=end

