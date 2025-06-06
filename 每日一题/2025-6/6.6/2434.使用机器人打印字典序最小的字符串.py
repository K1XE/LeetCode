#
# @lc app=leetcode.cn id=2434 lang=python3
#
# [2434] 使用机器人打印字典序最小的字符串
#
from mytools import *
# @lc code=start
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_suf = [None] * n
        min_suf[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suf[i] = min(min_suf[i + 1], s[i])
        res = []
        t = []
        i = 0
        for i in range(n):
            t.append(s[i])
            while t and (i == n - 1 or t[-1] <= min_suf[i + 1]):
                res.append(t.pop())
        return ''.join(res)
# @lc code=end

