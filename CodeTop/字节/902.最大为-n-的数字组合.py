#
# @lc app=leetcode.cn id=902 lang=python3
#
# [902] 最大为 N 的数字组合
#
import torch
from mytools import *
# @lc code=start
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        m = len(digits)
        s = str(n)
        k = len(s)
        dp = [[0] * 2 for _ in range(k + 1)]
        dp[0][1] = 1
        for i in range(1, k + 1):
            for d in digits:
                if d == s[i - 1]: dp[i][1] = dp[i - 1][1]
                elif d < s[i - 1]: dp[i][0] += dp[i - 1][1]
                else: break
            if i > 1: dp[i][0] += m + m * dp[i - 1][0]
        return sum(dp[k])
# @lc code=end

