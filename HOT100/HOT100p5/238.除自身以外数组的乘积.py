#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
from mytools import *
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cur = nums[:]
        n = len(nums)
        for i in range(n - 2, -1 , -1):
            cur[i] *= cur[i + 1]
        print(cur)
        print(nums)
        pre = 1
        for i in range(n):
            tmp = nums[i]
            nums[i] = pre * (cur[i + 1] if i + 1 < n else 1)
            pre *= tmp
        return nums
# @lc code=end

