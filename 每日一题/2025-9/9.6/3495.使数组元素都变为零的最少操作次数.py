#
# @lc app=leetcode.cn id=3495 lang=python3
#
# [3495] 使数组元素都变为零的最少操作次数
#
from mytools import *
# @lc code=start
class Solution:
    
    def minOperations(self, queries: List[List[int]]) -> int:
        def f(n):
            if n == 0: return 0
            m = n.bit_length()
            k = (m - 1) // 2 * 2
            res = (k << k >> 1) - (1 << k) // 3
            return res + (m + 1) // 2 * (n + 1 - (1 << k))
        return sum((f(r) - f(l - 1) + 1) // 2 for l, r in queries)
# @lc code=end

