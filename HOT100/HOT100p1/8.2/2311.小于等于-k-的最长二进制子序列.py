#
# @lc app=leetcode.cn id=2311 lang=python3
#
# [2311] 小于等于 K 的最长二进制子序列
#
from mytools import *
# @lc code=start
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        res = s.count('0')
        val = 0
        power = 0
        for i in range(n - 1, - 1, -1):
            if s[i] == '1':
                if power < 32:
                    if val + (1 << power) <= k:
                        val += 1 << power
                        res += 1
                power += 1
            else:
                power += 1
        return res
# @lc code=end

