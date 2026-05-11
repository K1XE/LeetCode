#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from mytools import *
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0
        res = 1
        cur = nums[0]
        if cur >= n - 1: return 1
        tmp = nums[0]
        for i in range(n):
            tmp = max(tmp, i + nums[i])
            if i >= cur:
                res += 1
                cur = tmp
                if cur >= n - 1: return res
# @lc code=end

