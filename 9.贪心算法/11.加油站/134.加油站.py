#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
from mytools import *
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0: return -1
        n = len(gas)
        sta = 0
        sums = 0
        for i in range(n):
            sums += gas[i] - cost[i]
            if sums < 0 :
                sums = 0
                sta = i + 1
        return sta
# @lc code=end

