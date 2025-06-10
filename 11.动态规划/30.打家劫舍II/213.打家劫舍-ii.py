#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
from mytools import *
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        def rob_line(arr):
            dp = arr[:]
            for i in range(len(arr)):
                dp[i] += max(dp[i - 2] if i - 2 >= 0 else 0, dp[i - 3] if i - 3 >= 0 else 0)
            return max(dp)
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))

# @lc code=end

