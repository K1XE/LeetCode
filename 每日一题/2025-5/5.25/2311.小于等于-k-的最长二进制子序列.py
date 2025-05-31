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
        cnt = 0
        v = 0
        p = 1
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                cnt += 1
            else:
                if v + p <= k:
                    v += p
                    cnt += 1
            p <<= 1
            if p > k:
                break
        for j in range(i - 1, -1, -1):
            if s[j] == '0': cnt += 1
        return cnt

# @lc code=end

