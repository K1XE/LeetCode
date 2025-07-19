#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
from mytools import *
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost): return -1
        idx = n - 1
        max_ = suf = gas[-1] - cost[-1]
        for i in range(n - 2, -1, -1):
            suf += gas[i] - cost[i]
            if suf > max_:
                max_ = suf
                idx = i
        return idx
# @lc code=end
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]
        suf = diff[:]
        for i in range(n - 2, -1, -1):
            suf[i] = diff[i] + suf[i + 1]
        if sum(diff) < 0: return -1
        res = suf.index(max(suf))
        return res
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        s = 0
        if sum(gas) < sum(cost): return -1
        res = 0
        for i in range(n):
            s += gas[i] - cost[i]
            if s < 0:
                res = i + 1
                s = 0
        return res
