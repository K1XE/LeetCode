#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
from mytools import *
# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        cnt = [0] * numCourses
        for p, q in prerequisites:
            g[q].append(p)
            cnt[p] += 1
        q = deque()
        for i in range(numCourses):
            if cnt[i] == 0: q.append(i)
        res = 0
        while q:
            cur = q.popleft()
            res += 1
            for p in g[cur]:
                cnt[p] -= 1
                if cnt[p] == 0: q.append(p)
        return res == numCourses
# @lc code=end

