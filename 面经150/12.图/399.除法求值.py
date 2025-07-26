#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
from typing import List
from collections import defaultdict
inf = float("inf")
# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        for (a, b), val in zip(equations, values):
            g[a].append((b, val))
            g[b].append((a, 1 / val))
        def dfs(u, tar, vis, prod):
            if u == tar: return prod
            vis.add(u)
            for v, w in g[u]:
                if v not in vis:
                    res = dfs(v, tar, vis, prod * w)
                    if res != -1.0: return res
            return -1.0
        res = []
        for a, b in queries:
            if a not in g or b not in g: res.append(-1.0)
            elif a == b: res.append(1.0)
            else:
                vis = set()
                res.append(dfs(a, b, vis, 1))
        return res
# @lc code=end

