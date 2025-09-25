#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
from mytools import *
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for x in nums:
            idx = bisect_left(res, x)
            if idx == len(res): res.append(x)
            else: res[idx] = x
        return len(res)
# @lc code=end

