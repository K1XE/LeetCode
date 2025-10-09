#
# @lc app=leetcode.cn id=3494 lang=python3
#
# [3494] 酿造药水需要的最少总时间
#
from mytools import *
# @lc code=start
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        lxt_finish = [0] * n
        for m in mana:
            s = 0
            for x, l in zip(skill, lxt_finish):
                if l > s: s = l
                s += x * m
            lxt_finish[-1] = s
            for i in range(n - 2, -1, -1):
                lxt_finish[i] = lxt_finish[i + 1] - skill[i + 1] * m
        return lxt_finish[-1]
# @lc code=end

