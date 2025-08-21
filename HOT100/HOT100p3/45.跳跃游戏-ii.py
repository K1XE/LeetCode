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
        nxt = cur = cnt = 0
        for i in range(n):
            nxt = max(nxt, i + nums[i])
            if i == cur:
                cnt += 1
                cur = nxt
                if cur >= n - 1: return cnt
        return cnt
# @lc code=end

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0
        nxt = 0
        res = 0
        for i in range(n):
            tmp = 0
            for j in range(i, nxt + 1):
                tmp = max(tmp, j + nums[j])
            nxt = tmp
            res += 1
            if nxt >= n - 1: return res
        return res