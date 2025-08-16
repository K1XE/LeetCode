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
        if n == 1: return True
        cur_co = nxt_co = 0
        for i, x in enumerate(nums):
            nxt_co = max(nxt_co, i + x)
            if i == cur_co:
                cur_co = nxt_co
                if cur_co >= n - 1: return True
        return False
# @lc code=end

