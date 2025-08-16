#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
from mytools import *
# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        sta, eds = newInterval
        while i < n and intervals[i][1] < sta:
            res.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= eds:
            sta = min(sta, intervals[i][0])
            eds = max(eds, intervals[i][1])
            i += 1
        res.append([sta, eds])
        for k in range(i, n): res.append(intervals[k])
        return res

# @lc code=end

