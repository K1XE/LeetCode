#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#
from mytools import *
# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        g = [[] for _ in range(len(rooms))]
        for u, packv in enumerate(rooms):
            for v in packv:
                g[u].append(v)
        self.cnt = 0
        vis = [False] * len(rooms)
        def dfs(u):
            vis[u] = True
            self.cnt += 1
            for v in g[u]:
                if not vis[v]:
                    dfs(v)
        dfs(0)
        return self.cnt == len(rooms)
# @lc code=end

