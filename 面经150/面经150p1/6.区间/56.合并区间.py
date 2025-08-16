#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from mytools import *
# @lc code=start
class DSU:
    def __init__(self):
        self.fa = []
        self.sz = []
    def find(self, x):
        if x != self.fa[x]: self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
    def union(self, a, b):
        if self.find(a) == self.find(b): return False
        else:
            a = self.find(a)
            b = self.find(b)
        if self.sz[b] > self.sz[a]:
            a, b = b, a
        a = self.fa[b]
        self.sz[a] += self.sz[b]
        return True
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        n = len(intervals)
        for i in range(1, n):
            if intervals[i][0] <= res[-1][1]: res[-1][1] = max(res[-1][1], intervals[i][1])
            else: res.append(intervals[i])
        return res
# @lc code=end

