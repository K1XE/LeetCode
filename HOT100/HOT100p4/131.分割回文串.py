#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
from mytools import *
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n): dp[i][i] = True
        for r in range(n):
            for l in range(r, -1, -1):
                if r - l < 3: dp[l][r] |= s[l] == s[r]
                else: dp[l][r] |= dp[l + 1][r - 1] and s[l] == s[r]
        res = []
        pack = []
        def dfs(sta):
            nonlocal n
            if sta == n:
                res.append(pack[:])
                return
            for i in range(sta, n):
                if not dp[sta][i]: continue
                pack.append(s[sta:i + 1])
                dfs(i + 1)
                pack.pop()
        dfs(0)
        return res
# @lc code=end

