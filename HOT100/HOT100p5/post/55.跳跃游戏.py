#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from mytools import *
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1 or nums[0] >= n - 1: return True
        if nums[0] == 0: return False
        cur = nums[0]
        tmp = nums[0]
        for i in range(n):
            tmp = max(tmp, i + nums[i])
            if i == cur:
                if tmp >= n - 1: return True
                cur = tmp
        return False
# @lc code=end

