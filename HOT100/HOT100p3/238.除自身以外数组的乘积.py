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
        res = nums[:]
        for i in range(n - 2, -1, -1):
            nums[i] *= nums[i + 1]
        pre = 1
        for i in range(n - 1):
            tmp = res[i]
            res[i] = nums[i + 1] * pre
            pre *= tmp
        res[-1] = pre
        return res
# @lc code=end

