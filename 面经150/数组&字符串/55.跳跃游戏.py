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
        cur = 0
        nxt = 0
        res = 0
        for i in range(n):
            nxt = max(nxt, i + nums[i])
            if cur == i:
                res += 1
                cur = nxt
                if nxt >= n - 1: return True
        return cur >= n - 1
# @lc code=end

