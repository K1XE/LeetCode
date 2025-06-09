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
        if sums_ % 2: return False
        t = sums_ // 2
        dp = [False] * (t + 1)
        dp[0] = True
        n = len(nums)
        for i in range(n):
            for j in range(t, nums[i] - 1, -1):
                dp[j] = dp[j - nums[i]] or dp[j]
        return dp[t]
# @lc code=end

