#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
from mytools import *
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, suf = 1, 1
        res = [1] * n
        for i in range(n):
            res[i] = pre
            pre *= nums[i]
        for i in range(n - 1, -1, -1):
            res[i] *= suf
            suf *= nums[i]
        return res
# @lc code=end

