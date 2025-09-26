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
        if s & 1: return False
        tar = s // 2
        dp = [0] * (tar + 1)
        for x in nums:
            for i in range(tar, x - 1, -1):
                dp[i] = max(dp[i], dp[i - x] + x)
        return dp[tar] == tar
# @lc code=end

