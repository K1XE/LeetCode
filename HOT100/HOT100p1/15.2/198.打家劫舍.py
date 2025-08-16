#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from mytools import *
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        pre1, pre2 = 0, 0
        for x in nums:
            cur = max(pre1, pre2 + x)
            pre2 = pre1
            pre1 = cur
        return max(pre1, pre2)
# @lc code=end

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums[:]
        for i in range(n):
            dp[i] += max(dp[i - 2] if i - 2 >= 0 else 0, dp[i - 3] if i - 3 >= 0 else 0)
        return max(dp)