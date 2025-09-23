#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
from mytools import *
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = [-1]
        n = len(heights)
        heights.append(0)
        res = 0
        for i in range(n):
            while stk[-1] != -1 and heights[i] < heights[stk[-1]]:
                cur = heights[stk.pop()]
                res = max(res, (i - stk[-1] - 1) * cur)
            stk.append(i)
        return res
# @lc code=end

