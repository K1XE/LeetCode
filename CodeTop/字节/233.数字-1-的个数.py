#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
from mytools import *
# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        high = list(map(int, str(n)))
        m = len(high)
        low = [0] * m
        @cache
        def dfs(i, limit_low, limit_high):
            if i == m: return (1, 0)
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9
            total_cnt = total_ones = 0
            for d in range(lo, hi + 1):
                cnt, ones = dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
                total_cnt += cnt
                total_ones += ones
                if d == 1: total_ones += cnt
            return (total_cnt, total_ones)
        return dfs(0, True, True)[1]
# @lc code=end

