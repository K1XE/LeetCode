#
# @lc app=leetcode.cn id=902 lang=python3
#
# [902] 最大为 N 的数字组合
#
from mytools import *
# @lc code=start
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        @cache
        def dfs(i, is_limits, is_num):
            if i == len(s):
                return int(is_num)
            res = 0
            if not is_num:
                res = dfs(i + 1, False, False)
            up = s[i] if is_limits else "9"
            for d in digits:
                if d > up: break
                res += dfs(i + 1, is_limits and d == up, True)
            return res
        return dfs(0, True, False)
# @lc code=end


