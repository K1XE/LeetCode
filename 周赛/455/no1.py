from mytools import *
class Solution:
    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        g = [[] for _ in range(n)]
        for u,v in edges: g[u].append(v); g[v].append(u)
        fa = [inf] * n
        stk, seq = [0], []
        while stk:
            u = stk.pop()
            seq.append(u)
            for v in g[u]:
                if v == fa[u]: continue
                fa[v] = u
                stk.append(v)
        foo = [0] * n
        res = 0
        for u in seq[::-1]:
            s = []
            for v in g[u]:
                if v == fa[u]: continue
                s.append(foo[v])
            if not s: 
                foo[u] = cost[u]
                continue
            mx = max(s)
            res += sum(1 for x in s if x < mx)
            foo[u] = cost[u] + mx
        return res