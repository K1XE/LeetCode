#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from mytools import *
# @lc code=start
class DSU:
    def __init__(self, n: int):
        self.fa = list(range(n))
        self.sz = [1] * n

    def find(self, x: int) -> int:
        if x != self.fa[x]: self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def unite(self, a: int, b: int) -> bool:
        a = self.find(a)
        b = self.find(b)
        if a == b: return False
        if self.sz[a] < self.sz[b]: a, b = b, a
        self.fa[b] = a
        self.sz[a] += self.sz[b]
        return True

    def isSame(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    def size(self, x: int) -> int:
        return self.sz[self.find(x)]

    def reset(self):
        n = len(self.fa)
        self.fa = list(range(n))
        self.sz = [1] * n

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        ss = set(nums)
        dsu = DSU(len(ss))
        idx = {}
        for i, x in enumerate(ss):
            idx[x] = i
        for x in ss:
            if x + 1 in ss: dsu.unite(idx[x], idx[x + 1])
        return max(dsu.size(i) for i in range(len(ss)))
# @lc code=end
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set(nums)
        res = 0
        for x in ss:
            if x - 1 not in ss:
                cur_res, cur_num = 1, x
                while cur_num + 1 in ss:
                    cur_res += 1
                    cur_num += 1
                res = max(res, cur_res)
        return res
