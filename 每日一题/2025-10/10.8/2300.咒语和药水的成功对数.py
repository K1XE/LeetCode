#
# @lc app=leetcode.cn id=2300 lang=python3
#
# [2300] 咒语和药水的成功对数
#
from mytools import *
# @lc code=start
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        n = len(potions)
        potions.sort()
        for s in spells:
            tar = success / s
            idx = bisect_left(potions, tar)
            if idx == n: res.append(0)
            else: res.append(n - idx)
        return res
# @lc code=end

