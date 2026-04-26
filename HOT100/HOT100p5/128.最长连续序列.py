#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from mytools import *
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        h = set(nums)
        for x in nums:
            if x not in h: continue
            cur = 1
            tmp = x
            while tmp - 1 in h: tmp -= 1; cur += 1; h.remove(tmp)
            tmp = x
            while tmp + 1 in h: tmp += 1; cur += 1; h.remove(tmp)
            res = max(res, cur)
        return res
# @lc code=end

