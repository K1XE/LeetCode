#
# @lc app=leetcode.cn id=3459 lang=python3
#
# [3459] 最长 V 形对角线段的长度
#
from mytools import *
# @lc code=start
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        dir_ = (1, 1), (1, -1), (-1, -1), (-1, 1)
        m, n = len(grid), len(grid[0])
        
        @cache
        def dfs(i, j, k, can_turn, tar):
            i += dir_[k][0]
            j += dir_[k][1]
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != tar: return 0
            res = dfs(i, j, k, can_turn, 2 ^ tar) + 1
            if can_turn: 
                max_ = (m - i, j + 1, i + 1, n - j)
                k = (k + 1) % 4
                if min(max_[k], max_[k - 1]) > res:
                    res = max(res, dfs(i, j, k, False, 2 ^ tar) + 1)
            return res
        res = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x != 1: continue
                max_ = (m - i, j + 1, i + 1, n - j)
                for k, mi in enumerate(max_):
                    if mi > res:
                        res = max(res, dfs(i, j, k, True, 2) + 1)
        return res
# @lc code=end

