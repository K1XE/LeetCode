#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from mytools import *
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = res = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            res = max(res, cur)
        return res
# @lc code=end

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = 0
        i = 0
        n = len(nums)
        ret = nums[0]
        for j in range(n):
            res += nums[j]
            ret = max(ret, res)
            while i <= j and res < 0:
                res -= nums[i]
                i += 1
        return ret