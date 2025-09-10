#
# @lc app=leetcode.cn id=1733 lang=python3
#
# [1733] 需要教语言的最少人数
#
from mytools import *
# @lc code=start
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        l = list(map(set, languages))
        pack = []
        for u, v in friendships:
            if l[u - 1].isdisjoint(l[v - 1]):
                pack.append((u - 1, v - 1))
        res = inf
        for i in range(1, n + 1):
            ss = set()
            for u, v in pack:
                if i not in l[u]: ss.add(u)
                if i not in l[v]: ss.add(v)
            res = min(res, len(ss))
        return res
# @lc code=end

