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
        cnt = [0] * numCourses
        for p, q in prerequisites:
            g[q].append(p)
            cnt[p] += 1
        q = deque()
        for i, x in enumerate(cnt):
            if x == 0: q.append(i)
        res = 0
        while q:
            cur = q.popleft()
            res += 1
            for u in g[cur]:
                cnt[u] -= 1
                if cnt[u] == 0: q.append(u)
        return numCourses == res
# @lc code=end

