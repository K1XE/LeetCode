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
        if n == 1: return 0
        cnt = 0
        cur = 0
        nxt = 0
        for i in range(n):
            nxt = max(nxt, i + nums[i])
            if i >= cur:
                cur = nxt
                cnt += 1
                if cur == n - 1: break
        return cnt
# @lc code=end

