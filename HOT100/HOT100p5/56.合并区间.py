#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from mytools import *
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        cur = 0
        n = len(intervals)
        if n <= 1: return intervals
        res = []
        intervals.sort()
        for i in range(1, n):
            tmp = intervals[i]
            if tmp[0] <= intervals[cur][-1]:
                if tmp[-1] > intervals[cur][-1]: intervals[cur][-1] = tmp[-1]
            else:
                res.append(intervals[cur])
                cur = i
        res.append(intervals[cur])
        return res
# @lc code=end

