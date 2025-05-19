#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from mytools import *
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cnt = 0
        res = float('-inf')
        for x in nums:
            cnt += x
            if cnt > res:
                res = cnt
            if cnt < 0: cnt = 0
        return res
# @lc code=end

