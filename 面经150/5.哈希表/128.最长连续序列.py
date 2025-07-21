#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from typing import List

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set(nums)
        res = 0
        for x in nums:
            if x not in ss: continue
            ss.remove(x)
            l = x - 1; r = x + 1
            while l in ss:
                ss.remove(l)
                l -= 1
            while r in ss:
                ss.remove(r)
                r += 1
            res = max(res, r - l - 1)
        return res
# @lc code=end

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set(nums)
        res = 0
        cnt = 0
        for x in nums:
            if x not in ss: continue
            if x - 1 not in ss:
                cnt = 1
                tmp = x
                ss.remove(tmp)
                while tmp + 1 in ss:
                    cnt += 1
                    ss.remove(tmp + 1)
                    tmp += 1
                res = max(res, cnt)
        return res