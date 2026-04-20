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
        res = [inf] * n
        for i in range(n):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                tmp = stk.pop()
                res[tmp] = i - tmp
            stk.append(i)
        return [x if x != inf else 0 for x in res]
# @lc code=end

