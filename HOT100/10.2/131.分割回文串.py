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
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i >= 2: dp[i][j] = dp[i + 1][j - 1]
                    else: dp[i][j] = True
                else: dp[i][j] = False
        pack = []
        res = []
        def dfs(sta):
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

