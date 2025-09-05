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
        for (a, b), val in zip(equations, values):
            g[a].append((b, val))
            g[b].append((a, 1 / val))
        def dfs(u, tar, vis, cur):
            if u == tar: return cur
            vis.add(u)
            for v, w in g[u]:
                if v not in vis:
                    res = dfs(v, tar, vis, cur * w)
                    if res != -1.0: return res
            return -1.0
        res = []
        for s, e in queries:
            if s not in g or e not in g: res.append(-1.0)
            elif s == e: res.append(1)
            else: res.append(dfs(s, e, set(), 1))
        return res
            
# @lc code=end

