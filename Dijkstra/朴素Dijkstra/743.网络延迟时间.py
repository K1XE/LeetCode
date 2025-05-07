#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#
from mytools import *
# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[float('inf') for _ in range(n)] for _ in range(n)]
        for u, v, w in times:
            g[u - 1][v - 1] = w
        dis = [float('inf')] * n
        res = dis[k - 1] = 0
        done = [False] * n
        while True:
            x = -1
            for i, ok in enumerate(done):
                if not ok and (x < 0 or dis[x] > dis[i]):
                    x = i
            if x < 0:
                return res
            if dis[x] == float('inf'):
                return -1
            res = dis[x]
            done[x] = True
            for y, w in enumerate(g[x]):
                dis[y] = min(dis[y], dis[x] + w)
# @lc code=end

