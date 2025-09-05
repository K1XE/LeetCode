#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
from mytools import *
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        slow = nums[slow]; fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
# @lc code=end

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i, x in enumerate(nums):
            while 0 <= nums[i] - 1 < n and nums[nums[i] - 1] != nums[i]: nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return nums[-1]