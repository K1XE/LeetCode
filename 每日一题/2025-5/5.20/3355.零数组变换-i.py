#
# @lc app=leetcode.cn id=3355 lang=python3
#
# [3355] 零数组变换 I
#
from mytools import *
# @lc code=start
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        cover = [0] * (n + 1)
        for l, r in queries:
            cover[l] += 1
            if r + 1 < n:
                cover[r + 1] -= 1 
        for i in range(n):
            if i > 0:
                cover[i] += cover[i - 1]
        for i in range(n):
            if cover[i] < nums[i]: return False
        return True
# @lc code=end

