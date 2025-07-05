#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from mytools import *
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        for x in nums:
            if cnt == 0:
                res = x
                cnt = 1
            elif x == res:
                cnt += 1
            else: cnt -= 1
        return res
# @lc code=end

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        for x in nums:
            if cnt == 0: res = x
            cnt += 1 if x == res else -1
        return res