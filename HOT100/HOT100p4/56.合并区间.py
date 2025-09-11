#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from mytools import *
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for s, e in intervals:
            if res and s <= res[-1][1]:
                if e > res[-1][1]: res[-1][1] = e
            else: res.append([s, e])
        return res
# @lc code=end

