#
# @lc app=leetcode.cn id=924 lang=python3
#
# [924] 尽量减少恶意软件的传播
#
from mytools import *
# @lc code=start
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        vis = [False] * n
        
        def dfs(node, comp):
            vis[node] = True
            comp.append(node)
            for i in range(n):
                if graph[node][i] == 1 and vis[i] == False:
                    dfs(i, comp)
        pack = []
        for i in range(n):
            if not vis[i]:
                comp = []
                dfs(i, comp)
                pack.append(comp)
        hacknode = {}
        for i, comp in enumerate(pack):
            for node in comp:
                hacknode[node] = i
        hackcnt = [0] * len(hacknode)
        for node in initial:
            idx = hacknode[node]
            hackcnt[idx] += 1
        initial.sort()
        max_saved = -1
        res = initial[0]
        for node in initial:
            idx = hacknode[node]
            if hackcnt[idx] == 1:
                saved = len(pack[idx])
                if saved > max_saved:
                    max_saved = saved
                    res = node
        return res
# @lc code=end

