#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from mytools import *
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        nxt_co = 0
        cur_co = 0
        n = len(nums)
        if n == 1: return 0
        for i in range(n):
            nxt_co = max(nxt_co, i + nums[i])
            if i == cur_co:
                res += 1
                cur_co = nxt_co
                if cur_co >= n - 1: break
        return res
# @lc code=end

