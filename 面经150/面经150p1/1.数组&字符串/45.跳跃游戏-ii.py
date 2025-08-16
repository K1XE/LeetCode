#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
from mytools import *
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = nxt = cnt = 0
        n = len(nums)
        if n <= 1: return 0
        for i in range(n):
            nxt = max(nxt, i + nums[i])
            if i == cur:
                cnt += 1
                cur = nxt
                if cur >= n - 1: break
        return cnt
# @lc code=end
class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = 0
        nxt = 0
        cnt = 0
        n = len(nums)
        if n <= 1: return 0
        for i in range(n):
            nxt = max(nxt, i + nums[i])
            if i >= cur:
                cnt += 1
                cur = nxt
                if cur >= n - 1: return cnt
        return cnt
