#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#
from mytools import *
# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in times:
            g[u - 1].append((v - 1, w))
        h = [(0, k - 1)]
        dis = [float('inf')] * n
        dis[k - 1] = 0
        heapq.heapify(h)
        while h:
            dist, node = heapq.heappop(h)
            if dist > dis[node]: continue
            for y, w in g[node]:
                if dis[y] > dist + w:
                    dis[y] = dist + w
                    heapq.heappush(h, (dis[y], y))
        res = 0
        for w in dis:
            if w == float('inf'): return -1
            res = max(w, res)
        return res
# @lc code=end

