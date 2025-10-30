#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
from mytools import *
# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        for (x, y), val in zip(equations, values):
            g[x].append((y, val))
            g[y].append((x, 1 / val))
        res = []
        def dfs(sta, tar, vis, cur):
            if sta == tar: return cur
            vis.add(sta)
            for v, w in g[sta]:
                if v not in vis:
                    x = dfs(v, tar, vis, cur * w)
                    if x != -1.: return x
            return -1.
        for u, v in queries:
            if u not in g or v not in g: res.append(-1.)
            elif u == v: res.append(1.)
            else: res.append(dfs(u, v, set(), 1.))
        return res
# @lc code=end

