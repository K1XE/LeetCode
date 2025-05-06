#
# @lc app=leetcode.cn id=1920 lang=python3
#
# [1920] 基于排列构建数组
#
from mytools import *
# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            ans.append(nums[x])
        return ans
# @lc code=end

