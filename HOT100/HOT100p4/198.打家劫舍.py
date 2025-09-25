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
        dp = [0] * n
        for i in range(n):
            dp[i] = max(dp[i - 3] if i - 3 >= 0 else 0, dp[i - 2] if i - 2 >= 0 else 0) + nums[i]
        return max(dp)
# @lc code=end

