#
# @lc app=leetcode.cn id=902 lang=python3
#
# [902] 最大为 N 的数字组合
#
from mytools import *
# @lc code=start
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        high = list(map(int, str(n)))
        m = len(high)
        digits = list(map(int, digits))
        @cache
        def dfs(i, limit_high, is_num):
            if i == m: return int(is_num)
            res = 0
            if not is_num: res += dfs(i + 1, False, False)
            hi = high[i] if limit_high else 9
            for d in digits:
                if d > hi: break
                res += dfs(i + 1, limit_high and d == hi, True)
            return res
        return dfs(0, True, False)
# @lc code=end

