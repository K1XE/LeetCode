#
# @lc app=leetcode.cn id=3354 lang=python3
#
# [3354] 使数组元素等于零
#
from mytools import *
# @lc code=start
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        pre = s = res = 0
        s = sum(nums)
        for x in nums:
            if x:
                pre += x
            elif pre * 2 == s: res += 2
            elif abs(pre * 2 - s) == 1: res += 1
        return res
# @lc code=end

