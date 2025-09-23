#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
from mytools import *
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [None] * n
        stk = []
        for i in range(n):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                res[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
        for i in range(n):
            if res[i] is None: res[i] = 0
        return res
# @lc code=end

