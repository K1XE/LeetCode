#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
from mytools import *
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for x in nums:
            idx = bisect.bisect_left(res, x)
            if idx == len(res): res.append(x)
            else: res[idx] = x
        return len(res)
# @lc code=end

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)