#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
from mytools import *
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n): dp[i][i] = True
        for r in range(n):
            for l in range(r, -1, -1):
                if r - l + 1<= 3: dp[l][r] |= s[l] == s[r]
                else: dp[l][r] |= s[l] == s[r] and dp[l + 1][r - 1]
        pack = []
        def dfs(i):
            nonlocal n
            if i >= n: res.append(pack.copy()); return
            for r in range(i, n):
                if not dp[i][r]: continue
                # print(pack)
                pack.append(s[i: r + 1])
                dfs(r + 1)
                pack.pop()
        dfs(0)
        return res
# @lc code=end

