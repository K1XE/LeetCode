#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
from mytools import *
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums_ = sum(nums)
        if sums_ & 1: return False
        t = sums_ // 2
        n = len(nums)
        dp = [False] * (t + 1)
        dp[0] = True
        for i, x in enumerate(nums):
            for j in range(t, x - 1, - 1):
                dp[j] = dp[j] | dp[j - x]
        return dp[t]
# @lc code=end

