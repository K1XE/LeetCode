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
        q = deque([x for x in range(numCourses) if ind[x] == 0])
        cnt = 0
        while q:
            cnt += 1
            cur = q.popleft()
            for v in g[cur]:
                ind[v] -= 1
                if ind[v] == 0: q.append(v)
        return cnt == numCourses
# @lc code=end

