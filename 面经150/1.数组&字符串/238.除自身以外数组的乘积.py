#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
from mytools import *
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums[:]
        n = len(nums)
        for i in range(n - 2, -1, -1): nums[i] *= nums[i + 1]
        pre = 1
        for i in range(0, n):
            tmp = res[i]
            res[i] = pre * (nums[i + 1] if i + 1 < n else 1)
            pre *= tmp
        return res
# @lc code=end

