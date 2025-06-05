#
# @lc app=leetcode.cn id=1061 lang=python3
#
# [1061] 按字典序排列最小的等效字符串
#
from mytools import *
# @lc code=start

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        fa = list(range(26))
        def find(x):
            if x == fa[x]: return x
            else: fa[x] = find(fa[x])
            return fa[x]
        def union(a, b):
            a, b = find(a), find(b)
            if a == b: return
            if a < b: a, b = b, a
            fa[a] = b
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))
        res = []
        for ch in baseStr:
            tmp = find(ord(ch) - ord('a'))
            res.append(chr(tmp + ord('a')))
        return ''.join(res)
# @lc code=end

