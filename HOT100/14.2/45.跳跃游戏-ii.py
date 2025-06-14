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
        cur_co = nxt_co = res = 0
        for i, x in enumerate(nums):
            nxt_co = max(nxt_co, i + x)
            if i == cur_co:
                cur_co = nxt_co
                res += 1
                if cur_co >= len(nums) - 1: return res
        return res
# @lc code=end

