#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
from mytools import *
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        q = deque([-1])
        n = len(heights)
        res = 0
        for i in range(n):
            while q[-1] != -1 and heights[q[-1]] > heights[i]:
                tmp = q.pop()
                res = max(res, (i - q[-1] - 1) * heights[tmp])
            q.append(i)
        return res
# @lc code=end

