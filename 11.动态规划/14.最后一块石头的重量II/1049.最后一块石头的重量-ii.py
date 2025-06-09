#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#
from mytools import *
# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sums_ = sum(stones)
        t = sums_ // 2
        dp = [0] * (t + 1)
        for s in stones:
            for j in range(t, s - 1, -1):
                dp[j] = max(dp[j], dp[j - s] + s)
        return abs(sums_ - 2 * dp[t])
# @lc code=end

