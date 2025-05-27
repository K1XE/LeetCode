#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
from mytools import *
# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        n = len(intervals)
        res = 0
        eds = intervals[0][1]
        for i in range(1, n):
            if eds <= intervals[i][0]: eds = intervals[i][1]
            else:
                eds = min(eds, intervals[i][1])
                res += 1
        return res
# @lc code=end
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        n = len(intervals)
        res = 0
        for i in range(1, n):
            if intervals[i][0] == intervals[i - 1][0]:
                res += 1
                intervals[i] = intervals[i - 1]
            else:
                if intervals[i][0] < intervals[i - 1][1]:
                    res += 1
                    if intervals[i][1] > intervals[i - 1][1]:
                        intervals[i] = intervals[i - 1]
        return res
