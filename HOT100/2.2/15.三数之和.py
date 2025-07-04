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
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l = i + 1; r = n - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    l += 1
                    r -= 1
                elif tmp > 0: r -= 1
                else: l += 1
        return res
# @lc code=end

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            ss = set()
            for j in range(i + 1, n):
                tar = - (nums[i] + nums[j])
                if tar in ss:
                    res.add(tuple(sorted((nums[i], nums[j], tar))))
                    while j + 1 < n and nums[j] == nums[j + 1]: j += 1
                ss.add(nums[j])
        return [list(tu) for tu in res]