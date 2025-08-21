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
            if x - 1 not in ss:
                cur = x
                cnt = 1
                while cur + 1 in ss:
                    ss.remove(cur)
                    cnt += 1
                    cur += 1
                res = max(res, cnt)
        return res

# @lc code=end

