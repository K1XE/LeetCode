#
# @lc app=leetcode.cn id=632 lang=python3
#
# [632] 最小区间
#
from mytools import *
# @lc code=start
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h = [(cur[0], i, 0) for i, cur in enumerate(nums)]
        heapify(h)
        resr = r = max(cur[0] for cur in nums)
        resl = h[0][0]
        while h[0][-1] + 1 < len(nums[h[0][1]]):
            _, i, j = h[0]
            x = nums[i][j + 1]
            heapreplace(h, (x, i, j + 1))
            r = max(r, x)
            l = h[0][0]
            if r - l < resr - resl: resr = r; resl = l
        return [resl, resr]
        
# @lc code=end

