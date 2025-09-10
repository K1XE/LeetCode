#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from mytools import *
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            tar = -nums[i]
            l, r = i + 1, n - 1
            while l < r:
                tmp = nums[l] + nums[r]
                if tmp == tar:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1; r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif tmp > tar:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                else:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
        return res 
# @lc code=end

