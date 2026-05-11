#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#
from mytools import *
# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n == 0: return 0
        b = [0] * (n + 1)
        for i in range(n):
            b[min(citations[i], n)] += 1
        s = 0
        for i in range(n, -1, -1):
            s += b[i]
            if s >= i: return i
        
# @lc code=end

