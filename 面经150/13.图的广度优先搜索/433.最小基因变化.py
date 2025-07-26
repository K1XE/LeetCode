#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
from mytools import *
# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque()
        q.append((startGene, 0))
        vis = set()
        vis.add(startGene)
        def diff(s1, s2):
            cnt = 0
            n = len(s1)
            for i in range(n):
                if s1[i] != s2[i]: cnt += 1
            return cnt
        while q:
            cur, step = q.popleft()
            if cur == endGene: return step
            for s in bank:
                if diff(cur, s) > 1: continue
                if s == endGene: return step + 1
                if s not in vis:
                    vis.add(s)
                    q.append((s, step + 1))
        return -1
# @lc code=end

