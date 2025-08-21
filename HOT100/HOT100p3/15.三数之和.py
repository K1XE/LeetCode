#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from mytools import *
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l = i + 1; r = n - 1
            tar = -nums[i]
            while l < r:
                cur = nums[l] + nums[r]
                if cur == tar:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l + 1] == nums[l]: l += 1
                    while l < r and nums[r - 1] == nums[r]: r -= 1
                    l += 1; r -= 1
                elif cur > tar:
                    while l < r and nums[r - 1] == nums[r]: r -= 1
                    r -= 1
                else:
                    while l < r and nums[l + 1] == nums[l]: l += 1
                    l += 1
        return res
# @lc code=end

