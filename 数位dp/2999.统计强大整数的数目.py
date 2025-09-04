#
# @lc app=leetcode.cn id=2999 lang=python3
#
# [2999] 统计强大整数的数目
#
from mytools import *
# @lc code=start
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        high = list(map(int, str(finish)))
        n = len(high)
        low = list(map(int, str(start).zfill(n)))
        diff = n - len(s)
        @cache
        def dfs(i, limit_low, limit_high):
            if i == n: return 1
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9
            res = 0
            if i < diff:
                for d in range(lo, min(hi, limit) + 1):
                    res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
            else:
                x = int(s[i - diff])
                if lo <= x <= hi:
                    res += dfs(i + 1, limit_low and x == lo, limit_high and x == hi)
            return res
        return dfs(0, True, True)
                
        
# @lc code=end

