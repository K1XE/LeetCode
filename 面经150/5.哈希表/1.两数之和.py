#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in hash: return [i, hash[target - nums[i]]]
            hash[nums[i]] = i
        return [-1, -1]
# @lc code=end

