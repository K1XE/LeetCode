#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from mytools import *
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = defaultdict(int)
        for i, x in enumerate(nums):
            if target - x in hash: return [i, hash[target - x]]
            hash[x] = i
# @lc code=end

