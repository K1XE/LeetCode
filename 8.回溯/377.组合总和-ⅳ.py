#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
from mytools import *
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], t: int) -> int:
        n = len(nums)
        res = 0
        @cache
        def dfs(t):
            nonlocal res
            if t == 0:
                return 1
            res = 0
            for i in range(0, n):
                if t - nums[i] < 0: break
                t -= nums[i]
                res += dfs(t)
                t += nums[i]
            return res
        nums.sort()
        dfs(t)
        return res
# @lc code=end

