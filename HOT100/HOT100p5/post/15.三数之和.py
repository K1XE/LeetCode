#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from mytools import *
# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if i - 1 >= 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, n - 1
            tar = -nums[i]
            while l < r:
                x = nums[l] + nums[r]
                if x == tar:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    l += 1
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    r -= 1
                elif x < tar:
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    l += 1
                else:
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    r -= 1
        return res
                    
# @lc code=end

