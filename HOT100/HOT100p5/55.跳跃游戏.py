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
        tmp = nums[0]
        cur = nums[0]
        for i in range(1, n):
            tmp = max(tmp, i + nums[i])
            if i == cur:
                cur = tmp
                if cur >= n - 1: return True
        return False
# @lc code=end

