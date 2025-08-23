#
# @lc app=leetcode.cn id=3197 lang=python3
#
# [3197] 包含所有 1 的最小矩形面积 II
#
from mytools import *
# @lc code=start
class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        def rot_():
            return list(zip(*reversed(grid)))
        def solve(g):
            def helper(g, ll, rr):
                l, r, t, b = inf, 0, inf, 0
                for i, row in enumerate(g):
                    for j, x in enumerate(row[ll:rr]):
                        if x: l, r, t, b = min(l, j), max(r, j), min(t, i), i
                return (r - l + 1) * (b - t + 1)
            res = inf
            m, n = len(g), len(g[0])
            if m >= 3:
                for i in range(1, m):
                    for j in range(i + 1, m):
                        area = helper(g[:i], 0, n)
                        area += helper(g[i:j], 0, n)
                        area += helper(g[j:], 0, n)
                        res = min(res, area)
            if m >= 2 and n >= 2:
                for i in range(1, m):
                    for j in range(1, n):
                        area = helper(g[:i], 0, n)
                        area += helper(g[i:], 0, j)
                        area += helper(g[i:], j, n)
                        res = min(res, area)
                        area = helper(g[:i], 0, j)
                        area += helper(g[:i], j, n)
                        area += helper(g[i:], 0, n)
                        res = min(res, area)
            return res
        return min(solve(grid), solve(rot_()))
# @lc code=end

