#
# @lc app=leetcode.cn id=837 lang=python3
#
# [837] 新 21 点
#

# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        s = 0.0
        dp = [0.0] * (n + 1)
        for i in range(n, -1, -1):
            dp[i] = 1.0 if i >= k else s / maxPts
            s += dp[i]
            if i + maxPts <= n: s -= dp[i + maxPts]
        return dp[0]
# @lc code=end

