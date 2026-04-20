#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
from mytools import *
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s_ = sum(nums)
        if s_ % 2: return False
        tar = s_ // 2
        dp = [[False] * (tar + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True 
        for i in range(1, len(nums) + 1):
            x = nums[i - 1]
            for j in range(tar + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= x:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - x]
        return dp[-1][tar]
# @lc code=end

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s_ = sum(nums)
        if s_ % 2: return False
        tar = s_ // 2
        dp = [False] * (tar + 1)
        dp[0] = True
        for x in nums:
            for j in range(tar, x - 1, -1):
                dp[j] = dp[j] or dp[j - x]
        return dp[tar]
        