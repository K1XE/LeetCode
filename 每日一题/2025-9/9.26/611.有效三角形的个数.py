#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#
from mytools import *
# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for k in range(n - 1, 1, -1):
            l, r = 0, k - 1
            while l < r:
                if nums[l] + nums[r] > nums[k]:
                    res += r - l
                    r -= 1
                else: l += 1
        return res
# @lc code=end

