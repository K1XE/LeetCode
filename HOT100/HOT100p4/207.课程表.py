#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
from mytools import *
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = [0] * numCourses
        g = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            g[v].append(u)
            d[u] += 1
        q = deque()
        for i in range(numCourses):
            if d[i] == 0: q.append(i)
        cnt = 0
        while q:
            idx = q.popleft()
            cnt += 1
            for v in g[idx]: 
                d[v] -= 1
                if d[v] == 0: q.append(v)
        return cnt == numCourses
                
# @lc code=end

