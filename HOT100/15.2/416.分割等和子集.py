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
        tar = sums_ // 2
        dp = [0] * (tar + 1)
        for x in nums:
            for j in range(tar, x - 1, -1):
                dp[j] = max(dp[j], dp[j - x] + x)
        return dp[tar] == tar
# @lc code=end

