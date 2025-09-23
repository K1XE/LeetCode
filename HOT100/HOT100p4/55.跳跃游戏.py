#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from mytools import *
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nxt = cur = 0
        res = 0
        for i, x in enumerate(nums):
            nxt = max(nxt, i + x)
            if cur == i:
                res += 1
                cur = nxt
                if cur >= len(nums) - 1: return True
        return False
# @lc code=end

