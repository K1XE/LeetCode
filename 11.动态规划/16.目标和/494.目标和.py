#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
from mytools import *
# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums_ = sum(nums)
        if (sums_ + target) % 2 or abs(target) > sums_: return 0
        t = sums_ + target >> 1
        dp = [0] * (t + 1)
        dp[0] = 1
        for x in nums:
            for j in range(t, x - 1, -1):
                dp[j] += dp[j - x]
        return dp[t]
# @lc code=end

