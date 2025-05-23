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
        res, ends, far = 0, 0, 0
        for i in range(0, n - 1):
            far = max(far, i + nums[i])
            if i == ends:
                res += 1
                ends = far
        return res
# @lc code=end

