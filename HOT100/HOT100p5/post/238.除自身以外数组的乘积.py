#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
from mytools import *
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp = nums[:]
        n = len(nums)
        for i in range(n - 2, - 1, - 1):
            tmp[i] *= tmp[i + 1]
        pre = 1
        for i in range(n):
            cur = nums[i]
            nums[i] = pre * (tmp[i + 1] if i + 1 <= n - 1 else 1)
            pre *= cur
        return nums
# @lc code=end

