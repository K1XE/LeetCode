#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from mytools import *
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        res = []
        i = 0
        while i < n:
            sta = nums[i]
            while i + 1 < n and nums[i + 1] - nums[i] == 1: i += 1
            eds = nums[i]
            res.append(f"{sta}->{eds}" if sta != eds else str(sta))
            i += 1
        return res

# @lc code=end

