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
            if x not in ss: continue
            tmp = 1
            u = x
            while u - 1 in ss: u -= 1; ss.remove(u); tmp += 1
            u = x
            while u + 1 in ss: u += 1; ss.remove(u); tmp += 1
            res = max(res, tmp)
        return res
# @lc code=end

