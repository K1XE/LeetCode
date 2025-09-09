#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from mytools import *
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        ss = set()
        res = 1
        for x in nums: ss.add(x)
        for x in nums:
            if x not in ss or x - 1 in ss: continue
            cur = x
            cnt = 1
            ss.remove(cur)
            while cur + 1 in ss:
                ss.remove(cur + 1)
                cnt += 1
                res = max(res, cnt)
                cur += 1
        return res
            
# @lc code=end

