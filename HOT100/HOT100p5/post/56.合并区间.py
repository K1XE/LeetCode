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
        idx = 0
        n = len(intervals)
        intervals.sort()
        if n <= 1: return intervals
        for i in range(1, n):
            if intervals[i][0] <= intervals[idx][-1]:
                if intervals[i][-1] > intervals[idx][-1]: intervals[idx][-1] = intervals[i][-1]
            else: res.append(intervals[idx]); idx = i
        res.append(intervals[idx])
        return res
                
# @lc code=end

