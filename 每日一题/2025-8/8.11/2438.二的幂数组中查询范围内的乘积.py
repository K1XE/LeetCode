#
# @lc app=leetcode.cn id=2438 lang=python3
#
# [2438] 二的幂数组中查询范围内的乘积
#
from mytools import *
# @lc code=start
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        tmp = []
        mod = 10**9 + 7
        for i in range(32):
            if n & 1 == 1: tmp.append(1 << i)
            n >>= 1
        pre = [1]
        n = len(tmp)
        for i in range(n): pre.append(tmp[i] * pre[-1])
        res = []
        for l, r in queries: res.append(pre[r + 1] * pow(pre[l], mod - 2, mod) % mod)
        return res
# @lc code=end

