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
        memo = [-1] * n
        def dfs(x):
            if x < 0 : return 0
            if memo[x] != -1: return memo[x]
            memo[x] = max(dfs(x - 1), dfs(x - 2) + nums[x])
            return memo[x]
        return dfs(n - 1)
# @lc code=end
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums
        for i in range(n):
            dp[i] += max(dp[i - 2] if i - 2 >= 0 else 0, dp[i - 3] if i - 3 >= 0 else 0)
        return max(dp)
