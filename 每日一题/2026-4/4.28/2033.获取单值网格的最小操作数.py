#
# @lc app=leetcode.cn id=2033 lang=python3
#
# [2033] 获取单值网格的最小操作数
#
from mytools import *
# @lc code=start
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = []
        tar = grid[0][0] % x
        for row in grid:
            for v in row:
                if v % x != tar: return -1
            a += row
        a.sort()
        mid = a[len(a) // 2]
        return sum(abs(v - mid) for v in a) // x
# @lc code=end

