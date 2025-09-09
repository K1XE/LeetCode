#
# @lc app=leetcode.cn id=2327 lang=python3
#
# [2327] 知道秘密的人数
#
from mytools import *
# @lc code=start
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 1_000_000_007
        s = [0] * (n + 1)
        s[1] = 1
        for i in range(2, n + 1):
            cur = s[max(0, i - delay)] - s[max(0, i - forget)]
            s[i] = (s[i - 1] + cur) % MOD
        return (s[n] - s[max(0, n - forget)]) % MOD
# @lc code=end

