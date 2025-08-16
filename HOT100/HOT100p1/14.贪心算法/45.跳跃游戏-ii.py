#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from mytools import *
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_co, nxt_co = 0, 0
        if len(nums) == 1: return 0
        res = 0
        for i in range(len(nums)):
            nxt_co = max(i + nums[i], nxt_co)
            if i == cur_co:
                res += 1
                cur_co = nxt_co
                if cur_co >= len(nums) - 1: break
        return res
# @lc code=end

