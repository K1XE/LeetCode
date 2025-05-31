#
# @lc app=leetcode.cn id=1007 lang=python3
#
# [1007] 行相等的最少多米诺旋转
#
from typing import List
# @lc code=start
class Solution:
    def minDominoRotations(self, ts: List[int], bs: List[int]) -> int:
        res = min(self.solve(ts, bs, ts[0]), self.solve(ts, bs, bs[0]))
        return res if res != float('inf') else -1
    def solve(self, ts, bs, tar):
        top, bot = 0, 0
        for i in range(len(ts)):
            if ts[i] != tar and bs[i] != tar:
                return float('inf')
            if ts[i] != tar: top += 1
            elif bs[i] != tar: bot += 1
        return min(top, bot)
# @lc code=end

