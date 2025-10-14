#
# @lc app=leetcode.cn id=3349 lang=python3
#
# [3349] 检测相邻递增子数组 I
#
from mytools import *
# @lc code=start
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(0, n - 1):
            dp[i + 1] = (dp[i] + 1) if nums[i + 1] > nums[i] else 1
            if dp[i + 1] >= k and i - k + 1 >= 0 and dp[i - k + 1] >= k: return True
        return False
# @lc code=end

