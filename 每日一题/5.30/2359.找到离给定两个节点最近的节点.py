#
# @lc app=leetcode.cn id=2359 lang=python3
#
# [2359] 找到离给定两个节点最近的节点
#
from mytools import *
# @lc code=start
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def calc_dis(node):
            n = len(edges)
            dis = [-1] * n
            vis = set()
            d = 0
            while node != -1 and node not in vis:
                dis[node] = d
                d += 1
                vis.add(node)
                node = edges[node]
            return dis
        dis1 = calc_dis(node1)
        dis2 = calc_dis(node2)
        res, ret = float('inf'), -1
        for i, (d1, d2) in enumerate(zip(dis1, dis2)):
            if d1 != -1 and d2 != -1:
                tmp = max(d1, d2)
                if tmp < res:
                    res = tmp
                    ret = i
        return ret
# @lc code=end

