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
        heights.append(0)
        n = len(heights)
        res = 0
        for i in range(n):
            while stk[-1] != -1 and heights[stk[-1]] > heights[i]:
                cur = stk.pop()
                res = max(res, heights[cur] * (i - stk[-1] - 1)) 
            stk.append(i)
        return res
                
# @lc code=end

