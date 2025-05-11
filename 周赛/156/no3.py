from mytools import *
class Solution(object):
    def maxWeight(self, n, edges, k, t):
        """
        :type n: int
        :type edges: List[List[int]]
        :type k: int
        :type t: int
        :rtype: int
        """
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
        res = [-1]
        def dfs(e, w_sum, u):
            if e == k:
                res[0] = max(res[0], w_sum)
            for v, w in g[u]:
                if w_sum + w < t:
                    w_sum += w
                    e += 1
                    dfs(e, w_sum, v)
                    e -= 1
                    w_sum -= w
        for i in range(n):
            dfs(0, 0, i)
        return res[0]
        

