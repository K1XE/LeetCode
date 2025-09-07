#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的 N 个不同整数
#
from mytools import *
# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n & 1: n -= 1; res.append(0)
        n //= 2
        idx = 1
        while n: res.append(idx); res.append(-idx); idx += 1; n -= 1
        return res
# @lc code=end

