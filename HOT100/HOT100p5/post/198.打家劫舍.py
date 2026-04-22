#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from mytools import *
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[-1]
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[-1])
# @lc code=end

