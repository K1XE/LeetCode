#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
from mytools import *
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        sta = 0
        s = 0
        for i in range(len(gas)):
            s += gas[i] - cost[i]
            if s < 0:
                sta = i + 1
                s = 0
        return sta
# @lc code=end

