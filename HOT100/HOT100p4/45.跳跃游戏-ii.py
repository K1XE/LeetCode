#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from mytools import *
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        res = 0
        nxt = cur = 0
        for i, x in enumerate(nums):
            nxt = max(nxt, i + x)
            if cur == i:
                res += 1
                cur = nxt
                if cur >= len(nums) - 1: return res
        return -1
# @lc code=end

