#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from mytools import *
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set(nums)
        res = 0
        for x in nums:
            if x not in ss or x - 1 in ss: continue
            cur = x
            tmp = 1
            while cur + 1 in ss:
                ss.remove(cur + 1)
                cur += 1
                tmp += 1
            res = max(res, tmp)
        return res
# @lc code=end

