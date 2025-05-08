#
# @lc app=leetcode.cn id=1514 lang=python3
#
# [1514] 概率最大的路径
#
from mytools import *
# @lc code=start
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        g = [[] for _ in range(n)]
        for (x, y), prob in zip(edges, succProb):
            g[x].append((y, prob))
            g[y].append((x, prob))
        prob = [0.0] * n
        prob[start_node] = 1.0
        h = [(-1.0, start_node)]
        while h:
            cur_prob, u = heapq.heappop(h)
            cur_prob = -cur_prob
            if u == end_node: return cur_prob
            for v, p in g[u]:
                if prob[v] < cur_prob * p:
                    prob[v] = cur_prob * p
                    heapq.heappush(h, (-prob[v], v))
        return 0.0

# @lc code=end

