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
        dp = nums
        for i in range(n):
            dp[i] += max(dp[i - 2] if i - 2 >= 0 else 0, \
                         dp[i - 3] if i - 3 >= 0 else 0)
        return max(dp)
# @lc code=end

