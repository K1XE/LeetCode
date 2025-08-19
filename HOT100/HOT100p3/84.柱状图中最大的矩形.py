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
        stk = [-1]
        res = 0
        for i in range(len(heights)):
            while stk[-1] != -1 and heights[i] < heights[stk[-1]]:
                tmp = stk.pop()
                res = max(res, heights[tmp] * (i - stk[-1] - 1))
            stk.append(i)
        return res
# @lc code=end

