#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
from mytools import *
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        slow, fast = nums[slow], nums[nums[fast]]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        fast = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return fast
# @lc code=end

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for a, b in pairwise(nums):
            if a == b: return a
        return -1