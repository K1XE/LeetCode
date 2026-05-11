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
        res = []
        for (s, e), x in zip(equations, values):
            g[s].append((e, x))
            g[e].append((s, 1 / x))
        def dfs(cur, tar, vis, x):
            if cur == tar: return x
            vis.add(cur)
            for v, w in g[cur]:
                if v not in vis:
                    tmp = dfs(v, tar, vis, x * w)
                    if tmp != -1.: return tmp
            return -1.
        for s, e in queries:
            if s not in g or e not in g: res.append(-1.)
            elif s == e: res.append(1.)
            else: res.append(dfs(s, e, set(), 1.))
        return res
            
        
# @lc code=end

