#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#
from mytools import *
# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind = [0] * numCourses
        g = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            ind[u] += 1
            g[v].append(u)
        q = deque([i for i in range(numCourses) if ind[i] == 0])
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in g[u]:
                ind[v] -= 1
                if ind[v] == 0: q.append(v)
        return res if len(res) == numCourses else []
# @lc code=end

