#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
from mytools import *
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(target + 1):
            for x in nums:
                if j >= x:
                    dp[j] += dp[j - x]
        return dp[target]
# @lc code=end

