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
        for (u, v), val in zip(equations, values):
            g[u].append((v, val))
            g[v].append((u, 1 / val))
        def dfs(sta, eds, vis, cur):
            if sta == eds: return cur
            vis.add(sta)
            for k, v in g[sta]:
                if k not in vis:
                    res = dfs(k, eds, vis, cur * v)
                    if res != -1.0: return res
            return -1.0
        res = []
        for x, y in queries:
            if x not in g: res.append(-1.0)
            elif x == y: res.append(1.0)
            else: res.append(dfs(x, y, set(), 1.0))
        return res
# @lc code=end

