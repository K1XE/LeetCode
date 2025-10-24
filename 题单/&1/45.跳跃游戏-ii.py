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
        cur = nxt = 0
        n = len(nums)
        if n <= 1: return 0
        for i in range(n):
            nxt = max(nxt, i + nums[i])
            if cur == i:
                res += 1
                cur = nxt
                if cur >= n - 1: return res
        
# @lc code=end

