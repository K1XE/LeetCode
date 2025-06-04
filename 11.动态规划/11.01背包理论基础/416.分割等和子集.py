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
        target = sums_ // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]) if j - nums[i - 1] >= 0 else dp[i - 1][j]
        return dp[n][target]
# @lc code=end

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums_ = sum(nums)
        if sums_ % 2: return False
        target = sums_ // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for x in nums:
            for j in range(target, x - 1, -1):
                dp[j] = dp[j] or dp[j - x]
        return dp[target]