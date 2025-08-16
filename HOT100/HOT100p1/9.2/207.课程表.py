#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
from mytools import *
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        ind = [0] * numCourses
        for u, v in prerequisites:
            g[v].append(u)
            ind[u] += 1
        q = deque()
        for i in range(numCourses):
            if ind[i] == 0: q.append(i)
        cnt = 0
        while q:
            u = q.popleft()
            cnt += 1
            for v in g[u]:
                ind[v] -= 1
                if ind[v] == 0: q.append(v)
        return cnt == numCourses
# @lc code=end

