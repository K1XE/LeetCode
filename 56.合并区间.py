#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from mytools import *
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for cur in intervals[1:]:
            if cur[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], cur[1])
            else: res.append(cur)
        return res
# @lc code=end

