#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
from mytools import *
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2: return False
        tar = s // 2
        n = len(nums)
        dp = [[False] * (tar + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(tar + 1):
                dp[i][j] |= dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] |= dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1]
# @lc code=end

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2: return False
        tar = s // 2
        dp = [0] * (tar + 1)
        for x in nums:
            for j in range(tar, x - 1, -1):
                dp[j] = max(dp[j], dp[j - x] + x)
        return dp[-1] == tar