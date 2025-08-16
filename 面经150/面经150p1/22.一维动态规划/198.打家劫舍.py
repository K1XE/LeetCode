#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from typing import List
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(n + 1):
            if i >= 2:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[n]
# @lc code=end

