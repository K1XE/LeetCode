#
# @lc app=leetcode.cn id=1857 lang=python3
#
# [1857] 有向图中最大颜色值
#
from mytools import *
# @lc code=start
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = [[] for _ in range(n)]
        for u, v in edges:
            if u == v: return -1
            g[u].append(v)
        memo = [None] * n
        def dfs(u):
            if memo[u] is not None: return memo[u]
            memo[u] = 0
            res = [0] * 26
            for v in g[u]:
                cv = dfs(v)
                if not cv: return cv
                for i in range(26):
                    res[i] = max(res[i], cv[i])
            res[ord(colors[u]) - ord('a')] += 1
            memo[u] = res
            return res
        ret = 0
        for u, c in enumerate(colors):
            res = dfs(u)
            if not res: return -1
            ret = max(ret, res[ord(c) - ord('a')])
        return ret
# @lc code=end

