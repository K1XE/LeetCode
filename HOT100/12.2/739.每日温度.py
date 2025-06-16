#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
from mytools import *
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                res[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
        return res
# @lc code=end

