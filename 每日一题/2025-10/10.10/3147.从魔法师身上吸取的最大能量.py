#
# @lc app=leetcode.cn id=3147 lang=python3
#
# [3147] 从魔法师身上吸取的最大能量
#
from mytools import *
# @lc code=start
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(len(energy) - k - 1, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)
# @lc code=end

