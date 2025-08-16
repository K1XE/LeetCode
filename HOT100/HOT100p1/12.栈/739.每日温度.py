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
        res = [0] * len(temperatures)
        stk.append(0)
        for i in range(1, len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                idx = stk.pop()
                res[idx] = i - idx
            stk.append(i)
        return res
# @lc code=end

