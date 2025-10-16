#
# @lc app=leetcode.cn id=2598 lang=python3
#
# [2598] 执行操作后的最大 MEX
#
from mytools import *
# @lc code=start
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = Counter(x % value for x in nums)
        mex = 0
        while cnt[mex % value]:
            cnt[mex % value] -= 1
            mex += 1
        return mex
# @lc code=end

